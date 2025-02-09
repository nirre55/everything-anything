def contribution_based_loot(damage_dealt):
    if damage_dealt > 1000:
        return "Loot rare obtenu!"
    else:
        return "Loot standard obtenu."


# Simulation
print(contribution_based_loot(1200))  # Dégâts infligés : 1200
