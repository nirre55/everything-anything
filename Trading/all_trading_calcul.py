import math


def calculer_marge_max(balance_usdt, risk_percent):
    """Calcule le montant risqué par trade (marge max)"""
    return balance_usdt * (risk_percent / 100)


def calculer_position_token(entry_price, stop_loss, marge_max):
    """Calcule la taille de position en token"""
    perte_par_unite = abs(entry_price - stop_loss)
    return round(marge_max / perte_par_unite, 6)


def calculer_position_usdt(entry_price, position_token):
    """Calcule la taille de position en USDT"""
    return round(position_token * entry_price, 2)


def calculer_levier(position_usdt, marge_max):
    """Calcule le levier requis pour utiliser toute la marge"""
    levier = position_usdt / marge_max
    return math.ceil(levier)


balance = 1000
risk = 10  # en %
entry = 27000
sl = 26500

marge = calculer_marge_max(balance, risk)
position_token = calculer_position_token(entry, sl, marge)
position_usdt = calculer_position_usdt(entry, position_token)
levier = calculer_levier(position_usdt, marge)

print("Marge max :", marge)
print("Taille de position (token) :", position_token)
print("Taille de position (USDT) :", position_usdt)
print("Levier requis :", levier)
