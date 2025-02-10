# loot_simulator/items.py


class Item:
    def __init__(self, name, rarity, category):
        self.name = name
        self.rarity = rarity
        self.category = category

    def __repr__(self):
        return f"{self.name} ({self.rarity}, {self.category})"
