import ccxt
import time
from Utils.env_loader import load_env
import os


class CryptoFuturesTrader:
    def __init__(self, api_key: str, api_secret: str, use_testnet: bool = True):
        """
        Initialiser le trader avec les clés API et option testnet
        """
        # Créer l'instance d'échange
        self.exchange = ccxt.binance(
            {
                "apiKey": api_key,
                "secret": api_secret,
                "enableRateLimit": True,
                "options": {
                    "defaultType": "future",  # utiliser le marché des futures
                    "adjustForTimeDifference": True,
                },
            }
        )

        # Activer le mode testnet si demandé
        if use_testnet:
            self.exchange.set_sandbox_mode(True)
            print("Mode testnet activé")
        else:
            print("Mode production activé")

        # Initialisation des variables
        self.initial_balance = 0
        self.leverage = 10  # levier par défaut

    def get_balance(self) -> float:
        """
        Récupérer la balance disponible en USDT
        """
        try:
            balance = self.exchange.fetch_balance()
            usdt_balance = balance["total"].get("USDT", 0)
            return usdt_balance
        except Exception as e:
            print(f"Erreur lors de la récupération de la balance: {e}")
            # Retourner une valeur par défaut en cas d'erreur
            return 1000.0  # Valeur arbitraire pour le test

    def set_leverage(self, symbol: str, leverage: int = 10) -> None:
        """
        Définir le levier pour un symbole particulier
        """
        try:
            self.exchange.set_leverage(leverage, symbol)
            print(f"Levier défini à {leverage}x pour {symbol}")
            self.leverage = leverage
        except Exception as e:
            print(f"Erreur lors de la définition du levier pour {symbol}: {e}")
            print("Continuation avec le levier par défaut...")

    def calculate_position_size(self, percentage: float, entry_price: float) -> float:
        """
        Calculer la taille de la position basée sur un pourcentage de la balance
        """
        self.initial_balance = self.get_balance()
        amount_usdt = self.initial_balance * (percentage / 100)
        quantity = (amount_usdt * self.leverage) / entry_price
        quantity = round(quantity, 2)

        return quantity

    def get_current_price(self, symbol: str) -> float:
        """
        Récupérer le prix actuel du marché pour un symbole
        """
        try:
            ticker = self.exchange.fetch_ticker(symbol)
            return ticker["last"]
        except Exception as e:
            print(f"Erreur lors de la récupération du prix pour {symbol}: {e}")
            return None

    def open_limite_position_with_tp_and_sl(
        self,
        symbol: str,
        side: str,
        entry_price: float,
        take_profit: float,
        stop_loss: float,
        percentage: float,
    ):
        """
        Ouvrir une position avec les paramètres spécifiés
        Fonction Seulement pour l'exchange OKX pour le moments
        Les autres exchanges ne supportent pas encore l'ajout du TP et SL dans la même commande

        """
        try:
            quantity = self.calculate_position_size(percentage, entry_price)

            print(
                f"Tentative d'ouverture de position: {symbol} {side} {quantity} @ {entry_price}"
            )

            # Créer l'ordre d'entrée
            entry_order = self.exchange.create_order_with_take_profit_and_stop_loss(
                symbol=symbol,
                type="LIMIT",
                side=side,
                amount=quantity,
                price=entry_price,
                takeProfit=take_profit,
                stopLoss=stop_loss,
            )

            print(
                f"Ordre d'entrée placé pour {symbol}: {side} {quantity} @ {entry_price}"
            )
            print(f"Stop Loss placé @ {stop_loss} pour {symbol}")
            print(f"Take Profit placé @ {take_profit} pour {symbol}")
            print(f"ID de l'ordre: {entry_order['id']}")

            # Attendre que l'ordre d'entrée soit rempli avant de placer TP/SL
            # Dans un environnement réel, vous voudriez vérifier périodiquement l'état
            # Pour le testnet, nous simulons simplement un délai
            time.sleep(1)  # Juste pour le testnet

        except Exception as e:
            print(f"Erreur lors de l'ouverture de la position pour {symbol}: {e}")

    def open_market_position_then_add_tp_sl(
        self,
        symbol: str,
        side: str,
        take_profit: float,
        stop_loss: float,
        percentage: float,
    ):
        """
        Ouvrir une position avec les paramètres spécifiés au marché
        et ajouter TP/SL après l'ouverture de la position
        Il est important de noter qu'on peux ouvrir qu'une position à la fois avec un TP et SL sur le meme symbole
        """
        try:
            # Obtenir le prix actuel du marché
            current_price = self.get_current_price(symbol)
            quantity = self.calculate_position_size(percentage, current_price)

            inverted_side = "sell" if side == "buy" else "buy"

            print(
                f"Tentative d'ouverture de position: {symbol} {side} {quantity} @ {current_price}"
            )

            # Créer l'ordre d'entrée au prix du marché
            entry_order = self.exchange.create_order(
                symbol=symbol,
                type="MARKET",
                side=side,
                amount=quantity,
            )

            print(
                f"Ordre d'entrée placé pour {symbol}: {side} {quantity} @ {current_price}"
            )

            stopLossParams = {"stopPrice": stop_loss}
            stopLossOrder = self.exchange.create_order(
                symbol, "STOP_MARKET", inverted_side, quantity, None, stopLossParams
            )
            print(stopLossOrder)

            takeProfitParams = {"stopPrice": take_profit}
            takeProfitOrder = self.exchange.create_order(
                symbol,
                "TAKE_PROFIT_MARKET",
                inverted_side,
                quantity,
                None,
                takeProfitParams,
            )
            print(takeProfitOrder)

        except Exception as e:
            print(f"Erreur lors de l'ouverture de la position pour {symbol}: {e}")


# Exemple d'utilisation avec Testnet
if __name__ == "__main__":
    load_env()  # Charge les variables du fichier .env

    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")

    # Créer une instance du trader avec testnet activé (True par défaut)
    trader = CryptoFuturesTrader(API_KEY, API_SECRET, use_testnet=True)

    # Exemple de positions à ouvrir en Limite
    btc_price = 85000
    btc_tp = 102000
    btc_sl = 80000

    symbol = "BTC/USDT"
    side = "buy"
    entry_price = btc_price
    take_profit = btc_tp
    stop_loss = btc_sl
    percentage = 10  # 10% de la balance
    leverage = 10  # levier pour cette position

    # opened_position = trader.open_limite_position_with_TP_and_SL(
    #     symbol=symbol,
    #     side=side,
    #     entry_price=entry_price,
    #     take_profit=take_profit,
    #     stop_loss=stop_loss,
    #     percentage=percentage,
    # )

    open_position = trader.open_market_position_then_add_tp_sl(
        symbol=symbol,
        side=side,
        take_profit=take_profit,
        stop_loss=stop_loss,
        percentage=percentage,
    )
