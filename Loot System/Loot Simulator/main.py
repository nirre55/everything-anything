# loot_simulator/main.py
import random
from loot_simulator.config import configure_loot
from loot_simulator.loot_simulator import LootSimulator
from loot_simulator.defeat_simulator import DefeatSimulator


def display_summary(rarity_summary, num_defeats):
    print(f"Résumé après {num_defeats} défaites :")
    for rarity, count in rarity_summary.items():
        print(f"- {rarity.capitalize()}: {count} objets")


def display_example_loots(total_loot, num_examples=5):
    print("\nExemples de loots obtenus :")
    for _ in range(num_examples):
        example_loot = random.sample(total_loot, min(5, len(total_loot)))
        print(f"Loot exemple : {example_loot}")


if __name__ == "__main__":
    # Configurer le loot
    config = configure_loot()

    # Initialiser le simulateur de loot
    loot_simulator = LootSimulator(config)

    # Simuler une défaite
    print("Simulation d'une défaite :")
    loot = loot_simulator.simulate_boss_loot()
    print(loot)

    # Simuler plusieurs défaites
    defeat_simulator = DefeatSimulator(loot_simulator)

    print("\nSimulation de 1000 défaites :")
    total_loot, rarity_summary = defeat_simulator.simulate_defeats(1000)
    display_summary(rarity_summary, 1000)

    print("\nSimulation de 10000 défaites :")
    total_loot, rarity_summary = defeat_simulator.simulate_defeats(10000)
    display_summary(rarity_summary, 10000)
