def evolving_loot(boss_kills):
    if boss_kills == 1:
        return "Loot standard obtenu."
    elif boss_kills == 5:
        return "Loot amélioré obtenu!"
    else:
        return "Continuez à combattre pour de meilleurs loots."


# Simulation
print(evolving_loot(5))  # Nombre de victoires : 5
