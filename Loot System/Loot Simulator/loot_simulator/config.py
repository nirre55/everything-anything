# loot_simulator/config.py


class LootConfig:
    def __init__(self):
        self.items = []
        self.rarity_drop_rates = {}
        self.max_items_per_rarity = {}

    def add_item(self, name, rarity, category):
        self.items.append({"name": name, "rarity": rarity, "category": category})

    def set_rarity_drop_rate(self, rarity, min_rate, max_rate):
        self.rarity_drop_rates[rarity] = {"min": min_rate, "max": max_rate}

    def set_max_items_per_rarity(self, rarity, max_items):
        self.max_items_per_rarity[rarity] = max_items


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
    config.set_rarity_drop_rate("légendaire", 0.01, 0.02)

    # Configurer les limites d'objets par rareté
    config.set_max_items_per_rarity("commun", 3)
    config.set_max_items_per_rarity("uncommun", 2)
    config.set_max_items_per_rarity("rare", 1)
    config.set_max_items_per_rarity("épique", 1)
    config.set_max_items_per_rarity("légendaire", 1)

    return config
