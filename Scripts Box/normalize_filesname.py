import os
import unicodedata
import re
from utils.path_utils import get_single_folder_path


def normalize_filename(filename):
    """
    Normalise le nom de fichier en retirant les accents et caractères spéciaux.
    Supprime également tout ce qui suit "_borders" et les caractères non alphanumériques (sauf les espaces).

    Args:
        filename (str): Nom de fichier à normaliser

    Returns:
        str: Nom de fichier normalisé
    """
    normalized = (
        unicodedata.normalize("NFKD", filename)
        .encode("ascii", "ignore")
        .decode("utf-8")
    )
    normalized = normalized.split("_borders")[
        0
    ]  # Supprimer tout ce qui suit "_borders"
    normalized = re.sub(
        r"[^a-zA-Z0-9 ]", "", normalized
    )  # Supprimer les caractères non alphanumériques sauf les espaces
    normalized = re.sub(
        r"\s+", " ", normalized
    ).strip()  # Supprimer les espaces en trop
    return normalized


def rename_files_in_folder(folder_path):
    """
    Renomme tous les fichiers d'un dossier en normalisant leurs noms.

    Args:
        folder_path (str): Chemin du dossier contenant les fichiers à renommer
    """
    if not os.path.isdir(folder_path):
        print("Le chemin spécifié n'est pas un dossier valide.")
        return

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)
            new_name = normalize_filename(name) + ext  # Conserver l'extension
            new_path = os.path.join(folder_path, new_name)

            if new_name and old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renommé: {filename} -> {new_name}")


# Exemple d'utilisation

folder_path = "png"

FOLDER_PATH = get_single_folder_path(folder_path)
rename_files_in_folder(FOLDER_PATH)
