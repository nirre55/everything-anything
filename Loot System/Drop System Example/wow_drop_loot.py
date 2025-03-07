import random
import json
import os

# Constantes
MIN_ITEMS = 3  # Nombre minimum d'objets par drop
MAX_ITEMS = 5  # Nombre maximum d'objets par drop
NUM_SIMULATIONS = 1000  # Nombre de simulations
NOMBRE_ELEMENTS = 259  # Nombre total d'objets

# Obtenir le dossier du script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "loot_simulation_results.txt")
PROB_FILE = os.path.join(SCRIPT_DIR, "probabilities.txt")

# Définir les raretés et leurs plages de probabilités
RARITIES = {
    "Commun": {"proportion": 0.40, "prob_range": (20.0, 40.0)},  # 40 %, 20% à 40%
    "Peu commun": {"proportion": 0.30, "prob_range": (10.0, 19.0)},  # 30 %, 10% à 19%
    "Rare": {"proportion": 0.20, "prob_range": (5.0, 9.0)},  # 20 %, 5% à 9%
    "Épique": {"proportion": 0.09, "prob_range": (1.0, 4.0)},  # 9 %, 1% à 4%
    "Légendaire": {"proportion": 0.01, "prob_range": (0.1, 0.9)},  # 1 %, 0.1% à 0.9%
}


# Fonction pour répartir les items
def distribute_items(total_items):
    counts = {}
    for rarity, info in RARITIES.items():
        counts[rarity] = int(total_items * info["proportion"])

    total_assigned = sum(counts.values())
    counts["Rare"] += total_items - total_assigned

    return counts


# Charger ou générer les probabilités
items_with_probs = {}
item_rarities = {}

if os.path.exists(PROB_FILE):
    # Charger les données depuis le fichier
    with open(PROB_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    ITEMS = data["items"]
    items_with_probs = {item: float(prob) for item, prob in data["probs"].items()}
    item_rarities = data["rarities"]
    print(f"Probabilités chargées depuis '{PROB_FILE}'.")
else:
    # Générer les items et les probabilités
    ITEMS = [str(i) for i in range(1, NOMBRE_ELEMENTS + 1)]
    random.shuffle(ITEMS)  # Mélanger les items aléatoirement

    counts = distribute_items(NOMBRE_ELEMENTS)
    index = 0
    for rarity, count in counts.items():
        for i in range(count):
            if index < len(ITEMS):
                item = ITEMS[index]
                prob = random.uniform(
                    RARITIES[rarity]["prob_range"][0], RARITIES[rarity]["prob_range"][1]
                )
                items_with_probs[item] = prob
                item_rarities[item] = rarity
                index += 1

    # Sauvegarder les données dans le fichier
    data = {"items": ITEMS, "probs": items_with_probs, "rarities": item_rarities}
    with open(PROB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Probabilités générées et sauvegardées dans '{PROB_FILE}'.")

# Initialiser le compteur des occurrences
item_counts = {item: 0 for item in ITEMS}


def simulate_loot_drop():
    dropped_items = []
    # Étape 1 : Tirer les objets selon leurs probabilités
    for item, prob in items_with_probs.items():
        if random.uniform(0, 100) <= prob:
            dropped_items.append(item)

    # Étape 2 : Si moins de MIN_ITEMS, retenter un tirage basé sur les probabilités
    while len(dropped_items) < MIN_ITEMS:
        for item, prob in items_with_probs.items():
            if item not in dropped_items and random.uniform(0, 100) <= prob:
                dropped_items.append(item)
                if len(dropped_items) >= MIN_ITEMS:
                    break

    # Étape 3 : Si plus de MAX_ITEMS, réduire aléatoirement à MAX_ITEMS
    if len(dropped_items) > MAX_ITEMS:
        dropped_items = random.sample(dropped_items, MAX_ITEMS)

    return dropped_items


def write_probabilities(file):
    file.write("Probabilités attribuées aux objets :\n")
    print("Probabilités attribuées aux objets :")
    for item in ITEMS:
        rarity = item_rarities[item]
        prob = items_with_probs[item]
        line = f"{item} ({rarity}): {prob:.2f}%\n"
        file.write(line)
        print(line.strip())


def run_simulations(file):
    file.write(f"Résultats des {NUM_SIMULATIONS} simulations :\n")
    for i in range(NUM_SIMULATIONS):
        result = simulate_loot_drop()
        sim_result = f"Simulation {i + 1} : {result}\n"
        file.write(sim_result)
        print(sim_result.strip())
        for item in result:
            item_counts[item] += 1


def write_statistics(file):
    file.write(f"\nStatistiques après {NUM_SIMULATIONS} simulations :\n")
    print(f"\nStatistiques après {NUM_SIMULATIONS} simulations :")
    for item in ITEMS:
        rarity = item_rarities[item]
        count = item_counts[item]
        percentage = (count / (NUM_SIMULATIONS * MAX_ITEMS)) * 100
        stat_line = f"{item} ({rarity}): {count} fois ({percentage:.2f}% des drops possibles, probabilité initiale: {items_with_probs[item]:.2f}%)\n"
        file.write(stat_line)
        print(stat_line.strip())

    total_items_dropped = sum(item_counts.values())
    avg_items_per_sim = total_items_dropped / NUM_SIMULATIONS
    file.write(f"Moyenne d'objets par simulation : {avg_items_per_sim:.2f}\n")
    print(f"Moyenne d'objets par simulation : {avg_items_per_sim:.2f}")

    # Statistiques par rareté
    file.write("\nStatistiques par rareté :\n")
    print("\nStatistiques par rareté :")
    for rarity in RARITIES:
        rarity_count = sum(
            item_counts[item] for item in ITEMS if item_rarities[item] == rarity
        )
        rarity_percentage = (
            (rarity_count / total_items_dropped) * 100 if total_items_dropped > 0 else 0
        )
        file.write(
            f"{rarity}: {rarity_count} fois ({rarity_percentage:.2f}% des drops totaux)\n"
        )
        print(
            f"{rarity}: {rarity_count} fois ({rarity_percentage:.2f}% des drops totaux)"
        )


# Exécution principale avec gestion des erreurs
try:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        write_probabilities(file)
        file.write("\n")
        run_simulations(file)
        write_statistics(file)
    print(f"\nLes résultats ont été enregistrés dans le fichier '{OUTPUT_FILE}'.")
except IOError as e:
    print(f"Erreur lors de l'écriture dans le fichier : {e}")
