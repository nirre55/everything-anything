import random


def loot_boss():
    # Définir les probabilités pour chaque objet
    rare_sword_chance = 0.10  # 10% de chance
    legendary_armor_chance = 0.02  # 2% de chance
    nothing_chance = 1 - rare_sword_chance - legendary_armor_chance  # 88% de chance

    # Générer un nombre aléatoire entre 0 et 1
    loot_roll = random.random()

    # Déterminer quel objet est obtenu en fonction du nombre aléatoire
    if loot_roll < legendary_armor_chance:
        return "Armure légendaire"
    elif loot_roll < legendary_armor_chance + rare_sword_chance:
        return "Épée rare"
    else:
        return "Rien"


# Simuler la défaite du boss plusieurs fois
def simulate_boss_defeats(num_defeats):
    results = {"Armure légendaire": 0, "Épée rare": 0, "Rien": 0}

    for _ in range(num_defeats):
        loot = loot_boss()
        results[loot] += 1

    return results


# Exemple d'utilisation
num_defeats = 1000
results = simulate_boss_defeats(num_defeats)

print(f"Résultats après {num_defeats} défaites du boss :")
for item, count in results.items():
    print(f"{item}: {count} fois ({count / num_defeats * 100:.2f}%)")
