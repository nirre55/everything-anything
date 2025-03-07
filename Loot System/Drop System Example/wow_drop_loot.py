"""
Loot Simulation System

This script simulates a loot drop system with predefined rarity categories,
generating items, assigning probabilities, and producing detailed statistics.
Probabilities are persisted in a JSON file for consistency across runs.
"""

import random
import json
import os
from typing import Dict, List, Tuple

# Configuration constants
MIN_ITEMS: int = 3
MAX_ITEMS: int = 5
NUM_SIMULATIONS: int = 1000
TOTAL_ITEMS: int = 259

# File paths (relative to script location)
SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE: str = os.path.join(SCRIPT_DIR, "loot_simulation_results.txt")
PROBABILITIES_FILE: str = os.path.join(SCRIPT_DIR, "probabilities.txt")

# Rarity definitions with proportions and probability ranges
RARITIES: Dict[str, Dict[str, float | Tuple[float, float]]] = {
    "Commun": {"proportion": 0.40, "prob_range": (20.0, 40.0)},
    "Peu commun": {"proportion": 0.30, "prob_range": (10.0, 19.0)},
    "Rare": {"proportion": 0.20, "prob_range": (5.0, 9.0)},
    "Épique": {"proportion": 0.09, "prob_range": (1.0, 4.0)},
    "Légendaire": {"proportion": 0.01, "prob_range": (0.1, 0.9)},
}


def distribute_items(total_items: int) -> Dict[str, int]:
    """
    Distribute items across rarity categories based on predefined proportions.

    Args:
        total_items: Total number of items to distribute.

    Returns:
        Dictionary mapping rarity categories to their item counts.
    """
    counts = {
        rarity: int(total_items * info["proportion"])
        for rarity, info in RARITIES.items()
    }
    assigned_total = sum(counts.values())
    counts["Rare"] += total_items - assigned_total  # Adjust Rare for remaining items
    return counts


def load_or_generate_probabilities() -> (
    Tuple[List[str], Dict[str, float], Dict[str, str]]
):
    """
    Load item probabilities and rarities from file or generate them if not present.

    Returns:
        Tuple of (items list, probabilities dict, rarities dict).
    """
    if os.path.exists(PROBABILITIES_FILE):
        with open(PROBABILITIES_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"Probabilities loaded from '{PROBABILITIES_FILE}'.")
        return (
            data["items"],
            {item: float(prob) for item, prob in data["probs"].items()},
            data["rarities"],
        )

    # Generate new items and probabilities
    items = [str(i) for i in range(1, TOTAL_ITEMS + 1)]
    random.shuffle(items)
    probabilities = {}
    rarities = {}
    counts = distribute_items(TOTAL_ITEMS)
    current_index = 0

    for rarity, count in counts.items():
        for _ in range(count):
            if current_index < len(items):
                item = items[current_index]
                min_prob, max_prob = RARITIES[rarity]["prob_range"]
                probabilities[item] = random.uniform(min_prob, max_prob)
                rarities[item] = rarity
                current_index += 1

    # Save to file
    data = {"items": items, "probs": probabilities, "rarities": rarities}
    with open(PROBABILITIES_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Probabilities generated and saved to '{PROBABILITIES_FILE}'.")

    return items, probabilities, rarities


def simulate_loot_drop(items: List[str], probabilities: Dict[str, float]) -> List[str]:
    """
    Simulate a single loot drop based on item probabilities.

    Args:
        items: List of all possible items.
        probabilities: Dictionary of item probabilities.

    Returns:
        List of dropped items (between MIN_ITEMS and MAX_ITEMS).
    """
    dropped_items = []
    for item in items:
        if random.uniform(0, 100) <= probabilities[item]:
            dropped_items.append(item)

    # Ensure minimum items
    available_items = [item for item in items if item not in dropped_items]
    while len(dropped_items) < MIN_ITEMS and available_items:
        for item in available_items[:]:  # Copy to modify during iteration
            if random.uniform(0, 100) <= probabilities[item]:
                dropped_items.append(item)
                available_items.remove(item)
                if len(dropped_items) >= MIN_ITEMS:
                    break

    # Limit to maximum items
    if len(dropped_items) > MAX_ITEMS:
        dropped_items = random.sample(dropped_items, MAX_ITEMS)

    return dropped_items


def write_probabilities(
    file, items: List[str], probabilities: Dict[str, float], rarities: Dict[str, str]
) -> None:
    """Write item probabilities and rarities to the output file and console."""
    file.write("Probabilités attribuées aux objets :\n")
    print("Probabilités attribuées aux objets :")
    for item in items:
        line = f"{item} ({rarities[item]}): {probabilities[item]:.2f}%\n"
        file.write(line)
        print(line.strip())


def run_simulations(
    file, items: List[str], probabilities: Dict[str, float], counts: Dict[str, int]
) -> None:
    """Run loot drop simulations and update item counts."""
    file.write(f"Résultats des {NUM_SIMULATIONS} simulations :\n")
    for i in range(NUM_SIMULATIONS):
        result = simulate_loot_drop(items, probabilities)
        sim_result = f"Simulation {i + 1} : {result}\n"
        file.write(sim_result)
        print(sim_result.strip())
        for item in result:
            counts[item] += 1


def write_statistics(
    file,
    items: List[str],
    probabilities: Dict[str, float],
    rarities: Dict[str, str],
    counts: Dict[str, int],
) -> None:
    """Write detailed statistics to the output file and console."""
    file.write(f"\nStatistiques après {NUM_SIMULATIONS} simulations :\n")
    print(f"\nStatistiques après {NUM_SIMULATIONS} simulations :")
    for item in items:
        count = counts[item]
        percentage = (count / (NUM_SIMULATIONS * MAX_ITEMS)) * 100
        stat_line = f"{item} ({rarities[item]}): {count} fois ({percentage:.2f}% des drops possibles, probabilité initiale: {probabilities[item]:.2f}%)\n"
        file.write(stat_line)
        print(stat_line.strip())

    total_dropped = sum(counts.values())
    avg_per_sim = total_dropped / NUM_SIMULATIONS
    file.write(f"Moyenne d'objets par simulation : {avg_per_sim:.2f}\n")
    print(f"Moyenne d'objets par simulation : {avg_per_sim:.2f}")

    file.write("\nStatistiques par rareté :\n")
    print("\nStatistiques par rareté :")
    for rarity in RARITIES:
        rarity_count = sum(counts[item] for item in items if rarities[item] == rarity)
        rarity_percentage = (
            (rarity_count / total_dropped * 100) if total_dropped > 0 else 0
        )
        rarity_line = f"{rarity}: {rarity_count} fois ({rarity_percentage:.2f}% des drops totaux)\n"
        file.write(rarity_line)
        print(rarity_line.strip())


def main() -> None:
    """Main function to orchestrate the loot simulation process."""
    try:
        items, probabilities, rarities = load_or_generate_probabilities()
        counts = {item: 0 for item in items}

        with open(OUTPUT_FILE, "w", encoding="utf-8") as output_file:
            write_probabilities(output_file, items, probabilities, rarities)
            output_file.write("\n")
            run_simulations(output_file, items, probabilities, counts)
            write_statistics(output_file, items, probabilities, rarities, counts)

        print(f"\nLes résultats ont été enregistrés dans le fichier '{OUTPUT_FILE}'.")
    except IOError as e:
        print(f"Erreur lors de l'accès aux fichiers : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")


if __name__ == "__main__":
    main()
