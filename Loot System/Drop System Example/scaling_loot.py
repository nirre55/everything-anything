def scaling_loot(player_level):
    loot_quality = min(player_level * 10, 100)  # Qualité du loot basée sur le niveau
    return f"Loot de qualité {loot_quality} obtenu."


# Simulation
print(scaling_loot(8))  # Niveau du joueur : 8
