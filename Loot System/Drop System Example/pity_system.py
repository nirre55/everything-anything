import random


def pity_system(attempts):
    rare_item_chance = min(attempts * 1, 100)  # Augmentation linéaire de la chance
    if random.randint(1, 100) <= rare_item_chance:
        return "Objet rare obtenu!"
    else:
        return "Pas de chance cette fois."


# Simulation
print(pity_system(50))  # Après 50 essais
