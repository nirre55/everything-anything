import os
import json
from utils.path_utils import get_folder_path
from utils.rename_image import rename_image_in_folder


def generate_json_metadata(images_folder, metadata_folder):
    """
    Parcourt un dossier d'images et génère un fichier JSON pour chaque image
    avec les métadonnées au format demandé.

    Args:
        images_folder (str): Chemin vers le dossier contenant les images
    """
    # S'assurer que le dossier de sortie existe
    os.makedirs(metadata_folder, exist_ok=True)

    # Récupérer tous les fichiers d'images dans le dossier
    image_files = [
        f
        for f in os.listdir(images_folder)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    # Trier les fichiers pour assurer un ordre cohérent
    image_files.sort()

    # Générer un fichier JSON pour chaque image
    for index, image_file in enumerate(image_files, start=1):
        # Extraire le nom de l'image sans l'extension
        base_name = os.path.splitext(image_file)[0]

        # Extraire IMAGE_NAME (en supprimant tout ce qui suit "_borders")
        image_name = base_name.split("_borders")[0]

        # Créer les métadonnées selon le format demandé
        metadata = {
            "id": index,
            "image": f"https://ipfs.io/ipfs/CID/{index}.png",
            "description": "my nft collection description",
            "attributes": [{"trait_type": "Name", "value": image_name}],
        }

        # Créer le fichier JSON
        output_file = os.path.join(metadata_folder, f"{index}.json")
        with open(output_file, "w") as f:
            json.dump(metadata, f, indent=4)

        print(f"Métadonnées générées pour {image_file} -> {output_file}")
        rename_image_in_folder(images_folder, image_file, f"{index}")

    print(
        f"Génération terminée. {len(image_files)} fichiers JSON ont été créés dans {metadata_folder}"
    )


if __name__ == "__main__":

    input_folder = "images"
    output_folder = "metadata"

    IMAGES_FOLDER, METADATA_FOLDER = get_folder_path(input_folder, output_folder)

    # Vérifier si le dossier existe
    if not os.path.isdir(IMAGES_FOLDER):
        print(f"Erreur: Le dossier '{IMAGES_FOLDER}' n'existe pas.")
    else:
        generate_json_metadata(IMAGES_FOLDER, METADATA_FOLDER)
