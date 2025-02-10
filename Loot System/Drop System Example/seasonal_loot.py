def seasonal_loot(season):
    if season == "Hiver":
        return "Skin d'hiver obtenu!"
    else:
        return "Pas de skin spécial cette saison."


# Simulation
print(seasonal_loot("Hiver"))
