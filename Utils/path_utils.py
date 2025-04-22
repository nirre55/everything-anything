import os
import sys


def get_folder_path(input_dir: str, output_dir: str):
    """Génère les chemins des dossiers d'entrée et de sortie en fonction du script exécuté."""
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(script_dir, input_dir), os.path.join(script_dir, output_dir)


def get_single_folder_path(folder_name: str):
    """Retourne le chemin d'un seul dossier basé sur le script exécuté."""
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(script_dir, folder_name)
