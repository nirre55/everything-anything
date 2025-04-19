import ccxt
import time
from typing import List, Dict, Any
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

    def calculate_position_size(
        self, percentage: float, entry_price: float, symbol: str
    ) -> float:
        """
        Calculer la taille de la position basée sur un pourcentage de la balance
        """
        amount_usdt = self.initial_balance * (percentage / 100)

        try:
            # Convertir le montant USDT en quantité de l'actif
            symbol_info = self.exchange.market(symbol)
            precision = symbol_info["precision"]["amount"]

            # Correction: s'assurer que precision est bien un entier
            if isinstance(precision, float):
                precision = int(precision)

            # Calculer la quantité en tenant compte du levier
            quantity = (amount_usdt * self.leverage) / entry_price
            quantity = round(quantity, precision)

            return quantity
        except Exception as e:
            print(f"Erreur lors du calcul de la taille de position: {e}")
            # Calculer une taille approximative en cas d'erreur
            quantity = (amount_usdt * self.leverage) / entry_price
            return round(quantity, 3)  # Arrondir à 3 décimales par défaut

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

    def open_position(
        self,
        symbol: str,
        side: str,
        entry_price: float,
        take_profit: float,
        stop_loss: float,
        percentage: float,
    ) -> Dict[str, Any]:
        """
        Ouvrir une position avec les paramètres spécifiés
        """
        try:
            quantity = self.calculate_position_size(percentage, entry_price, symbol)

            print(
                f"Tentative d'ouverture de position: {symbol} {side} {quantity} @ {entry_price}"
            )

            # Créer l'ordre d'entrée
            entry_order = self.exchange.create_limit_order(
                symbol=symbol, side=side, amount=quantity, price=entry_price
            )

            print(
                f"Ordre d'entrée placé pour {symbol}: {side} {quantity} @ {entry_price}"
            )
            print(f"ID de l'ordre: {entry_order['id']}")

            # Attendre que l'ordre d'entrée soit rempli avant de placer TP/SL
            # Dans un environnement réel, vous voudriez vérifier périodiquement l'état
            # Pour le testnet, nous simulons simplement un délai
            time.sleep(1)  # Juste pour le testnet

            # Identifier le côté opposé pour les ordres TP/SL
            tp_side = "sell" if side == "buy" else "buy"

            # Vérifier que le prix TP est réaliste par rapport au prix du marché
            current_price = self.get_current_price(symbol) or entry_price

            # Pour long: TP > current, Pour short: TP < current
            valid_tp_price = take_profit
            if side == "buy" and take_profit <= current_price:
                valid_tp_price = current_price * 1.01  # 1% au-dessus
            elif side == "sell" and take_profit >= current_price:
                valid_tp_price = current_price * 0.99  # 1% en-dessous

            # Placer le take profit
            try:
                # Ne pas utiliser reduceOnly pour le premier ordre après une entrée
                tp_params = (
                    {}
                )  # Les TP/SL sur Binance Futures n'utilisent pas toujours reduceOnly

                tp_order = self.exchange.create_limit_order(
                    symbol=symbol,
                    side=tp_side,
                    amount=quantity,
                    price=valid_tp_price,
                    params=tp_params,
                )
                print(f"Take Profit placé @ {valid_tp_price} pour {symbol}")
            except Exception as e:
                print(f"Erreur lors du placement du Take Profit: {e}")
                tp_order = None

            # Placer le stop loss - correction de la signature de la méthode
            try:
                # Pour les ordres stop, il faut utiliser stopPrice et price
                sl_params = {
                    "stopPrice": stop_loss,
                }

                # Utiliser la bonne méthode: create_order avec stop market order
                sl_order = self.exchange.create_order(
                    symbol=symbol,
                    type="STOP_MARKET",  # Type d'ordre pour stop market
                    side=tp_side,
                    amount=quantity,
                    params=sl_params,
                )
                print(f"Stop Loss placé @ {stop_loss} pour {symbol}")
            except Exception as e:
                print(f"Erreur lors du placement du Stop Loss: {e}")
                sl_order = None

            return {
                "symbol": symbol,
                "side": side,
                "entry_order": entry_order,
                "tp_order": tp_order,
                "sl_order": sl_order,
                "quantity": quantity,
            }

        except Exception as e:
            print(f"Erreur lors de l'ouverture de la position pour {symbol}: {e}")
            return {}

    def open_multiple_positions(
        self, positions_data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Ouvrir plusieurs positions selon les données fournies
        """
        # Mettre à jour la balance initiale
        self.initial_balance = self.get_balance()
        print(f"Balance initiale: {self.initial_balance} USDT")

        results = []

        for position in positions_data:
            symbol = position["symbol"]
            side = position["side"]

            # Obtenir le prix actuel du marché
            current_price = self.get_current_price(symbol)

            # Si entry_price est None ou 0, utiliser le prix actuel
            entry_price = position.get("entry_price")
            if not entry_price or entry_price == 0:
                if current_price:
                    # Ajuster légèrement le prix pour que l'ordre soit exécuté
                    entry_price = (
                        current_price * 1.001
                        if side == "buy"
                        else current_price * 0.999
                    )
                    print(f"Utilisation du prix actuel pour {symbol}: {entry_price}")
                else:
                    print(
                        f"Impossible d'obtenir le prix pour {symbol}, position ignorée"
                    )
                    continue

            # Calculer TP et SL basés sur le prix d'entrée si non spécifiés
            take_profit = position.get("take_profit")
            if not take_profit:
                take_profit = (
                    entry_price * 1.02 if side == "buy" else entry_price * 0.98
                )

            stop_loss = position.get("stop_loss")
            if not stop_loss:
                stop_loss = entry_price * 0.98 if side == "buy" else entry_price * 1.02

            percentage = position.get("percentage", 5.0)
            leverage = position.get("leverage", self.leverage)

            # Définir le levier pour ce symbole
            self.set_leverage(symbol, leverage)

            # Ouvrir la position
            result = self.open_position(
                symbol=symbol,
                side=side,
                entry_price=entry_price,
                take_profit=take_profit,
                stop_loss=stop_loss,
                percentage=percentage,
            )

            if result:
                results.append(result)

        return results


# Exemple d'utilisation avec Testnet
if __name__ == "__main__":
    load_env()  # Charge les variables du fichier .env

    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")

    # Créer une instance du trader avec testnet activé (True par défaut)
    trader = CryptoFuturesTrader(API_KEY, API_SECRET, use_testnet=True)

    # Afficher les marchés disponibles
    try:
        markets = trader.exchange.load_markets()
        print(
            f"Marchés chargés avec succès. Nombre de marchés disponibles: {len(markets)}"
        )
    except Exception as e:
        print(f"Erreur lors du chargement des marchés: {e}")

    # Récupérer les prix actuels pour les symboles d'intérêt
    btc_price = trader.get_current_price("BTC/USDT") or 60000
    eth_price = trader.get_current_price("ETH/USDT") or 3000

    print(f"Prix actuels: BTC/USDT = {btc_price}, ETH/USDT = {eth_price}")

    # Définir les positions à ouvrir avec des prix basés sur les prix courants
    positions = [
        {
            "symbol": "BTC/USDT",
            "side": "buy",
            "entry_price": btc_price
            * 0.995,  # Juste en-dessous du prix actuel pour un ordre limit
            "take_profit": btc_price * 1.02,  # +2%
            "stop_loss": btc_price * 0.98,  # -2%
            "percentage": 5.0,  # 5% de la balance
            "leverage": 10,  # levier pour cette position
        },
        {
            "symbol": "ETH/USDT",
            "side": "sell",  # position short
            "entry_price": eth_price
            * 1.005,  # Juste au-dessus du prix actuel pour un ordre limit short
            "take_profit": eth_price * 0.97,  # -3%
            "stop_loss": eth_price * 1.03,  # +3%
            "percentage": 3.0,  # 3% de la balance
        },
    ]

    # Ouvrir toutes les positions
    opened_positions = trader.open_multiple_positions(positions)

    print(f"Nombre de positions ouvertes: {len(opened_positions)}")
    for pos in opened_positions:
        print(f"Position {pos['symbol']} {pos['side']} ouverte avec succès")
