def guaranteed_drop(boss_name):
    if boss_name == "Boss Final":
        return "Clé de la victoire obtenue!"
    else:
        return "Pas de clé cette fois."


# Simulation
print(guaranteed_drop("Boss Final"))
