import random
from collections import defaultdict


# Classe pour représenter un objet
class Item:
    def __init__(self, name, rarity, category):
        self.name = name
        self.rarity = rarity
        self.category = category

    def __repr__(self):
        return f"{self.name} ({self.rarity}, {self.category})"


# Classe pour gérer la configuration des loots
class LootConfig:
    def __init__(self):
        self.items = []
        self.rarity_drop_rates = {}
        self.max_items_per_rarity = {}

    def add_item(self, name, rarity, category):
        self.items.append(Item(name, rarity, category))

    def set_rarity_drop_rate(self, rarity, min_rate, max_rate):
        self.rarity_drop_rates[rarity] = {"min": min_rate, "max": max_rate}

    def set_max_items_per_rarity(self, rarity, max_items):
        self.max_items_per_rarity[rarity] = max_items


# Classe pour simuler le loot
class LootSimulator:
    def __init__(self, config):
        self.config = config

    def does_item_drop(self, rarity):
        if rarity not in self.config.rarity_drop_rates:
            return False
        rate_range = self.config.rarity_drop_rates[rarity]
        drop_rate = random.uniform(rate_range["min"], rate_range["max"])
        return random.random() * 100 < drop_rate

    def simulate_boss_loot(self):
        loot = []
        # La clé drop toujours
        loot.append(Item("Clé du boss", "spécial", "clé"))

        # Nombre d'objets à drop (entre 3 et 6)
        num_items = random.randint(3, 6)

        # Compteur pour suivre le nombre d'objets par rareté
        rarity_counts = defaultdict(int)

        # Sélectionner les objets qui drop
        dropped_items = 0
        while dropped_items < num_items:
            item = random.choice(self.config.items)
            rarity = item.rarity

            # Vérifier si on peut encore ajouter un objet de cette rareté
            if rarity_counts[rarity] < self.config.max_items_per_rarity.get(
                rarity, float("inf")
            ):
                if self.does_item_drop(rarity):
                    loot.append(item)
                    rarity_counts[rarity] += 1
                    dropped_items += 1

        return loot


# Classe pour simuler plusieurs défaites
class DefeatSimulator:
    def __init__(self, loot_simulator):
        self.loot_simulator = loot_simulator

    def simulate_defeats(self, num_defeats):
        total_loot = []
        rarity_summary = defaultdict(int)

        for _ in range(num_defeats):
            loot = self.loot_simulator.simulate_boss_loot()
            total_loot.extend(loot)
            for item in loot:
                rarity_summary[item.rarity] += 1

        return total_loot, rarity_summary


# Fonction pour afficher un résumé des loots
def display_summary(rarity_summary, num_defeats):
    print(f"Résumé après {num_defeats} défaites :")
    for rarity, count in rarity_summary.items():
        print(f"- {rarity.capitalize()}: {count} objets")


# Fonction pour afficher des exemples de loots
def display_example_loots(total_loot, num_examples=5):
    print("\nExemples de loots obtenus :")
    for _ in range(num_examples):
        example_loot = random.sample(total_loot, min(5, len(total_loot)))
        print(f"Loot exemple : {example_loot}")


# Configuration des loots
def configure_loot():
    config = LootConfig()

    # Ajouter les objets
    config.add_item("Épée rouillée", "commun", "arme")
    config.add_item("Bouclier en bois", "commun", "armure")
    config.add_item("Potion de soin mineure", "commun", "consommable")
    config.add_item("Arc court", "commun", "arme")
    config.add_item("Chapeau de voyageur", "commun", "armure")
    config.add_item("Anneau de cuivre", "uncommun", "accessoire")
    config.add_item("Dague tranchante", "uncommun", "arme")
    config.add_item("Cape légère", "uncommun", "armure")
    config.add_item("Potion de mana mineure", "uncommun", "consommable")
    config.add_item("Bottes en cuir", "uncommun", "armure")
    config.add_item("Épée en argent", "rare", "arme")
    config.add_item("Bouclier enchanté", "rare", "armure")
    config.add_item("Potion de soin supérieure", "rare", "consommable")
    config.add_item("Anneau d'argent", "rare", "accessoire")
    config.add_item("Arc long", "rare", "arme")
    config.add_item("Armure en mithril", "épique", "armure")
    config.add_item("Épée légendaire", "légendaire", "arme")
    config.add_item("Amulette des anciens", "légendaire", "accessoire")
    config.add_item("Potion de résurrection", "épique", "consommable")
    config.add_item("Cape d'invisibilité", "épique", "armure")

    # Configurer les taux de drop
    config.set_rarity_drop_rate("commun", 50, 60)
    config.set_rarity_drop_rate("uncommun", 30, 40)
    config.set_rarity_drop_rate("rare", 10, 20)
    config.set_rarity_drop_rate("épique", 1, 5)
    config.set_rarity_drop_rate("légendaire", 0.01, 0.2)

    # Configurer les limites d'objets par rareté
    config.set_max_items_per_rarity("commun", 3)
    config.set_max_items_per_rarity("uncommun", 2)
    config.set_max_items_per_rarity("rare", 1)
    config.set_max_items_per_rarity("épique", 1)
    config.set_max_items_per_rarity("légendaire", 1)

    return config


# Programme principal
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
