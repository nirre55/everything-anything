def crafting_system(materials):
    if materials >= 5:
        return "Épée forgée avec succès!"
    else:
        return "Pas assez de matériaux."


# Simulation
print(crafting_system(6))  # Nombre de matériaux : 6
