import random
import json
import os

# Définition du chemin du script et des fichiers
SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))
DISTRIBUTION_FILE: str = os.path.join(SCRIPT_DIR, "distribution.json")


def load_probabilities():
    """Charge les probabilités à partir d'un fichier JSON."""
    if not os.path.exists(DISTRIBUTION_FILE):
        print(f"Erreur : Le fichier '{DISTRIBUTION_FILE}' n'existe pas.")
        return {}

    try:
        with open(DISTRIBUTION_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            items = json.loads(content)
            print(f"Fichier chargé avec succès. {len(items)} objets trouvés.")
            # Créer un dictionnaire avec l'ID de l'objet comme clé et un dictionnaire contenant le poids et la catégorie comme valeur
            return {
                item["id"]: {
                    "poids": float(item["poids"]),
                    "categorie": item["categorie"],
                }
                for item in items
            }
    except json.JSONDecodeError as e:
        print(f"Erreur JSON invalide : {str(e)}")
        return {}
    except Exception as e:
        print(f"Erreur lors du chargement : {str(e)}")
        return {}


def get_random_drop(probabilities):
    """Sélectionne un objet au hasard en respectant les pondérations."""
    if not probabilities:
        return None

    # Extraire les objets et leurs poids
    objects = list(probabilities.keys())
    weights = [item["poids"] for item in probabilities.values()]

    return random.choices(objects, weights=weights, k=1)[0]


def simulate_drops(probabilities, num_drops):
    """Simule plusieurs tirages pour observer la répartition des objets et enregistre les résultats."""
    if not probabilities:
        print("Aucune probabilité chargée.")
        return

    # Créer le fichier de résultats avec le nom basé sur num_drops
    RESULTS_FILE: str = os.path.join(SCRIPT_DIR, f"simulation_results_{num_drops}.txt")

    # Simuler les tirages
    results = {}
    category_results = {}  # Dictionnaire pour stocker les résultats par catégorie
    for _ in range(num_drops):
        item = get_random_drop(probabilities)
        if item:
            # Mettre à jour les résultats par objet
            results[item] = results.get(item, 0) + 1

            # Mettre à jour les résultats par catégorie
            category = probabilities[item]["categorie"]
            category_results[category] = category_results.get(category, 0) + 1

    # Écrire les résultats dans le fichier (mode 'w' pour écraser le fichier existant)
    with open(RESULTS_FILE, "w", encoding="utf-8") as file:
        file.write(f"Résultats de {num_drops} tirages :\n\n")

        # Écrire les résultats par objet
        file.write("=== Répartition par objet ===\n")
        for item, count in sorted(results.items()):
            percentage = (count / num_drops) * 100
            original_prob = probabilities[item]["poids"]
            result_line = f"Objet {item}: {count} fois ({percentage:.2f}%) - Probabilité théorique: {original_prob}% - Catégorie: {probabilities[item]['categorie']}\n"
            file.write(result_line)
            print(result_line)

        # Écrire les résultats par catégorie
        file.write("\n=== Répartition par catégorie ===\n")
        for category, count in sorted(category_results.items()):
            percentage = (count / num_drops) * 100
            result_line = f"Catégorie {category}: {count} fois ({percentage:.2f}%)\n"
            file.write(result_line)
            print(result_line)

    print(f"Résultats enregistrés dans '{RESULTS_FILE}'\n")


if __name__ == "__main__":
    print(f"Dossier du script : {SCRIPT_DIR}")
    probs = load_probabilities()

    if probs:
        single_drop = get_random_drop(probs)
        if single_drop:
            print(f"Drop unique : Objet {single_drop}")

        simulate_drops(probs, 10000)
