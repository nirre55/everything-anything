def location_based_loot(location):
    if location == "Forêt Enchantée":
        return "Arc légendaire obtenu!"
    else:
        return "Pas de loot spécial ici."


# Simulation
print(location_based_loot("Forêt Enchantée"))
