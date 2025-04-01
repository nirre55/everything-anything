import json
import sys
from pathlib import Path
from utils.path_utils import get_folder_path, get_single_folder_path


def update_json_files_with_rarity(data_folder: str, metadata_folder: str, rarity: str):
    try:
        data_file = Path(data_folder) / f"{rarity}-items.json"

        # Lire le fichier JSON source
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            number = item.get("number")
            if number is None:
                continue

            json_file = Path(metadata_folder) / f"{number}.json"
            if json_file.exists():
                with open(json_file, "r", encoding="utf-8") as f:
                    content = json.load(f)

                # Vérifier si 'attributes' existe et est une liste
                if "attributes" not in content or not isinstance(
                    content["attributes"], list
                ):
                    content["attributes"] = []

                # Ajouter l'attribut Rarety
                content["attributes"].append({"trait_type": "Rarety", "value": rarity})

                # Écrire les modifications dans le fichier
                with open(json_file, "w", encoding="utf-8") as f:
                    json.dump(content, f, indent=4, ensure_ascii=False)
                print(f"Fichier {json_file} mis à jour avec Rarety: {rarity}")
            else:
                print(f"Fichier {json_file} introuvable.")
    except Exception as e:
        print(f"Erreur: {e}")


def add_attribute_json_files(metadata_folder: str, trait_type: str, trait_value):
    try:
        metadata_path = Path(metadata_folder)
        if not metadata_path.exists() or not metadata_path.is_dir():
            print(
                f"Le dossier {metadata_folder} n'existe pas ou n'est pas un dossier valide."
            )
            return

        for json_file in metadata_path.glob("*.json"):
            with open(json_file, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Vérifier si 'attributes' existe et est une liste
            if "attributes" not in content or not isinstance(
                content["attributes"], list
            ):
                content["attributes"] = []

            # Ajouter l'attribut personnalisé
            content["attributes"].append(
                {"trait_type": trait_type, "value": trait_value}
            )

            # Écrire les modifications dans le fichier
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(content, f, indent=4, ensure_ascii=False)
            print(f"Fichier {json_file} mis à jour avec {trait_type}: {trait_value}")
    except Exception as e:
        print(f"Erreur: {e}")


def remove_key(metadata_folder: str, key: str):
    try:
        metadata_path = Path(metadata_folder)
        if not metadata_path.exists() or not metadata_path.is_dir():
            print(
                f"Le dossier {metadata_folder} n'existe pas ou n'est pas un dossier valide."
            )
            return

        for json_file in metadata_path.glob("*.json"):
            with open(json_file, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Supprimer la clé 'image' si elle existe
            if key in content:
                del content[key]
                print(f"Clé {key} supprimée dans {json_file}")

                # Écrire les modifications dans le fichier
                with open(json_file, "w", encoding="utf-8") as f:
                    json.dump(content, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erreur: {e}")


if __name__ == "__main__":
    rarety_folder = "rarety-items"  # Dossier contenant data.json
    metadata_folder = "metadata"  # Dossier contenant les fichiers JSON à modifier

    METADATA_FOLDER = get_single_folder_path(metadata_folder)

    # rarity = "Common"
    # update_json_files_with_rarity(RARETY_FOLDER, METADATA_FOLDER, rarity)

    # trait_type = "Epoch"
    # trait_value = 1
    # add_attribute_json_files(METADATA_FOLDER, trait_type, trait_value)

    remove_key(METADATA_FOLDER, "image")
