import random
from collections import Counter


def attribuer_rarete(nombres, rarete_config):
    """
    Attribue une rareté à chaque élément de la liste `nombres` en fonction des proportions définies dans `rarete_config`.
    Retourne une liste de dictionnaires contenant le nombre et sa rareté.
    """
    # Calculer le nombre total d'éléments
    total_elements = len(nombres)

    # Générer les proportions aléatoirement dans les plages spécifiées
    proportions = {}
    for rarete, config in rarete_config.items():
        if "range" in config:  # Vérifier si la clé "range" existe
            min_prop, max_prop = config["range"]
            proportions[rarete] = random.uniform(min_prop, max_prop)
        elif "fixed" in config:  # Si la rareté a un nombre fixe d'éléments
            proportions[rarete] = 0  # Pas besoin de proportion pour les raretés fixes

    # Normaliser les proportions pour qu'elles somment à 1 (100%)
    total_proportions = sum(proportions.values())
    for rarete in proportions:
        proportions[rarete] /= total_proportions

    # Calculer le nombre d'éléments pour chaque rareté
    rarete_elements = {}
    for rarete, prop in proportions.items():
        if rarete_config[rarete].get("fixed"):
            # Si le nombre d'éléments est fixe (ex: Legendaire)
            rarete_elements[rarete] = rarete_config[rarete]["fixed"]
        else:
            # Sinon, calculer en fonction de la proportion
            rarete_elements[rarete] = int(total_elements * prop)

    # S'assurer que le total des éléments attribués ne dépasse pas la taille de la liste
    total_attribue = sum(rarete_elements.values())
    if total_attribue > total_elements:
        # Ajuster la rareté avec la plus grande proportion
        rarete_max = max(rarete_elements, key=lambda x: rarete_elements[x])
        rarete_elements[rarete_max] -= total_attribue - total_elements

    # Mélanger la liste pour une attribution aléatoire
    random.shuffle(nombres)

    # Attribuer les raretés
    resultat = []
    index = 0
    for rarete, count in rarete_elements.items():
        for _ in range(count):
            resultat.append({"nombre": nombres[index], "rareté": rarete})
            index += 1

    return resultat


def generer_epoch(epoch_id, epoch_nom, nombres, rarete_config):
    """
    Génère une epoch avec un identifiant, un nom, et le résultat de l'attribution des raretés.
    """
    resultat = attribuer_rarete(nombres, rarete_config)
    return {
        "epoch_id": epoch_id,
        "epoch_nom": epoch_nom,
        "resultat": resultat,
        "repartition": Counter(element["rareté"] for element in resultat),
    }


# Configuration des raretés
rarete_config = {
    "Commun": {"range": (0.45, 0.55)},  # Entre 45% et 55%
    "Uncommon": {"range": (0.30, 0.40)},  # Entre 30% et 40%
    "Rare": {"range": (0.10, 0.20)},  # Entre 10% et 20%
    "Epique": {"range": (0.03, 0.07)},  # Entre 3% et 7%
    "Legendaire": {"fixed": random.randint(1, 2)},  # Entre 1 et 2 éléments
}

# Liste de nombres (peut être modifiée)
nombres = list(range(151))

# Générer plusieurs epochs
epochs = []
for i in range(1, 6):  # Générer 5 epochs
    epoch_nom = f"Epoch {i}"
    epoch = generer_epoch(i, epoch_nom, nombres, rarete_config)
    epochs.append(epoch)

# Afficher les résultats pour chaque epoch
for epoch in epochs:
    print(f"\nEpoch ID: {epoch['epoch_id']}, Nom: {epoch['epoch_nom']}")
    print("Répartition des raretés:", epoch["repartition"])
    # print("Résultat final:")
    # for element in epoch["resultat"]:
    #     print(f"Nombre: {element['nombre']}, Rareté: {element['rareté']}")
