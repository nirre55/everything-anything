import random
import json
import os

SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))
DISTRIBUTION_FILE: str = os.path.join(SCRIPT_DIR, "distribution.json")


def generate_random_weights(total_objects):
    categories = {
        "commun": {"percentage": 0.40, "range": (20, 40)},
        "uncommun": {"percentage": 0.30, "range": (10, 19)},
        "rare": {"percentage": 0.20, "range": (5, 9)},
        "epique": {"percentage": 0.09, "range": (1, 4)},
        "legendaire": {"percentage": 0.01, "range": (0.1, 0.9)},
    }

    # Générer la liste des objets
    objects = [f"objet_{i+1}" for i in range(total_objects)]
    random.shuffle(objects)  # Mélange les objets

    distribution = []
    index = 0

    for category, data in categories.items():
        count = int(
            total_objects * data["percentage"]
        )  # Nombre d'objets pour cette catégorie
        for _ in range(count):
            if index < total_objects:
                weight = round(random.uniform(*data["range"]), 1)
                distribution.append((objects[index], weight, category))
                index += 1

    # Assigner les objets restants à la catégorie "rare"
    while index < total_objects:
        weight = round(random.uniform(*categories["rare"]["range"]), 1)
        distribution.append((objects[index], weight, "rare"))
        index += 1

    # Sauvegarde dans un fichier JSON
    with open(DISTRIBUTION_FILE, "w", encoding="utf-8") as file:
        json.dump(
            [
                {"id": obj, "poids": weight, "categorie": cat}
                for obj, weight, cat in distribution
            ],
            file,
            indent=4,
        )

    print(f"Fichier 'distribution.json' généré avec {len(distribution)} objets.")


# Exemple avec 103 objets
generate_random_weights(256)
