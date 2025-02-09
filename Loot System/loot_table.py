import random


def loot_table():
    loot = {"Potion": 50, "Armure": 30, "Arme": 20}
    return random.choices(list(loot.keys()), weights=loot.values(), k=1)[0]


# Simulation
print(f"Le boss a lâché : {loot_table()}")
