import os
import xml.etree.ElementTree as ET
import shutil
from pathlib import Path


def remove_text_element(source_folder, destination_folder):
    # Créer le dossier de destination s'il n'existe pas
    os.makedirs(destination_folder, exist_ok=True)

    # Définir le namespace SVG
    namespaces = {"svg": "http://www.w3.org/2000/svg"}
    # Enregistrer le namespace pour éviter le préfixe dans les balises sauvegardées
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

    # Pour chaque fichier dans le dossier source
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".svg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            try:
                # Charger le fichier SVG
                tree = ET.parse(source_path)
                root = tree.getroot()

                # Trouver tous les éléments g avec id="text_1"
                found = False
                for parent in root.findall(".//*"):
                    for element in parent.findall('./svg:g[@id="text_1"]', namespaces):
                        parent.remove(element)
                        found = True
                    # Chercher aussi sans le namespace en cas de fichier SVG sans namespace défini
                    for element in parent.findall('./g[@id="text_1"]'):
                        parent.remove(element)
                        found = True

                # Sauvegarder le fichier modifié
                tree.write(destination_path)
                print(
                    f"Traité: {filename} {'(éléments supprimés)' if found else '(aucun élément trouvé)'}"
                )

            except Exception as e:
                print(f"Erreur avec le fichier {filename}: {e}")
                # Copier le fichier original en cas d'erreur
                shutil.copy2(source_path, destination_path)


if __name__ == "__main__":
    # Définir les dossiers source et destination
    SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))
    input_dir = "svg"
    output_dir = "svg-without-text"

    OUTPUT_FOLDER: str = os.path.join(SCRIPT_DIR, output_dir)
    INPUT_FOLDER: str = os.path.join(SCRIPT_DIR, input_dir)

    remove_text_element(INPUT_FOLDER, OUTPUT_FOLDER)
    print(
        f"Traitement terminé. Les fichiers modifiés sont enregistrés dans {OUTPUT_FOLDER}"
    )
