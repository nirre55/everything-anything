# loot_simulator/loot_simulator.py

import random
from loot_simulator.items import Item
from loot_simulator.config import LootConfig


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
        rarity_counts = {rarity: 0 for rarity in self.config.rarity_drop_rates}

        # Sélectionner les objets qui drop
        dropped_items = 0
        while dropped_items < num_items:
            item_data = random.choice(self.config.items)
            item = Item(item_data["name"], item_data["rarity"], item_data["category"])
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
