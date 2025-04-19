import os
import subprocess
from Utils.path_utils import get_folder_path


def convert_svgs_to_png(
    input_folder: str, output_folder: str, width: int = 300, height: int = 300
):
    """
    Convertit tous les fichiers SVG d'un dossier en PNG avec Inkscape et ajuste leur taille.

    :param input_folder: Dossier contenant les fichiers SVG.
    :param output_folder: Dossier où enregistrer les PNG.
    :param width: Largeur de l'image en pixels (défaut 300).
    :param height: Hauteur de l'image en pixels (défaut 300).
    """
    # Vérifie si le dossier de sortie existe, sinon le créer
    os.makedirs(output_folder, exist_ok=True)

    # Liste des fichiers SVG dans le dossier
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".svg"):  # Vérifie que c'est un fichier SVG
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)

            try:
                command = [
                    "inkscape",
                    f"--export-filename={output_path}",
                    f"--export-width={width}",
                    f"--export-height={height}",
                    input_path,
                ]
                subprocess.run(command, check=True)
                print(f"✅ Converti : {input_path} → {output_path} ({width}x{height})")

            except Exception as e:
                print(f"❌ Erreur lors de la conversion de {filename} : {e}")


input_dir = "svg-without-text"
output_dir = "png"

INPUT_FOLDER, OUTPUT_FOLDER = get_folder_path(input_dir, output_dir)

convert_svgs_to_png(INPUT_FOLDER, OUTPUT_FOLDER, width=300, height=300)
