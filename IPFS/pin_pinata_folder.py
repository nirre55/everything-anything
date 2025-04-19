import requests
import json
import os
from pathlib import Path
from Utils.env_loader import load_env
from Utils.path_utils import get_folder_path

# Charge les variables d'environnement
load_env()

# Vos clés API Pinata
PINATA_JWT = os.getenv("jwk_key")

# Remplacez par votre JWT Pinata
PINATA_API_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"

# Headers avec l'authentification JWT
headers = {"Authorization": f"Bearer {PINATA_JWT}"}


def pin_folder_to_ipfs(folder_name, folder_path, extensions):
    try:
        # Vérifier que le dossier local existe
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"Le dossier {folder_path} n'existe pas")

        files_to_upload = [
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
            and f.lower().endswith(extensions)
        ]

        if not files_to_upload:
            raise ValueError(f"Aucune image trouvée dans {folder_path}")

        # Préparer les fichiers avec le chemin relatif "images/"
        files = [
            ("file", (f"{folder_name}/{Path(file).name}", open(file, "rb")))
            for file in files_to_upload
        ]

        # Métadonnées Pinata
        pinata_folder_name = json.dumps({"name": folder_name})
        data = {"pinataMetadata": pinata_folder_name}

        # Faire la requête POST
        response = requests.post(
            PINATA_API_URL, headers=headers, files=files, data=data
        )

        # Vérifier la réponse
        response.raise_for_status()
        res_data = response.json()
        print("Résultat de l'upload :", json.dumps(res_data, indent=2))

        # URL d'accès au dossier
        ipfs_hash = res_data["IpfsHash"]
        print(f"Accès au dossier : https://ipfs.io/ipfs/{ipfs_hash}/{folder_name}/")

        return ipfs_hash

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'upload : {e}")
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")


def replace_cid_in_json(directory, replacement):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                file_path = os.path.join(directory, filename)
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                json_str = json.dumps(data)
                updated_json_str = json_str.replace("CID", replacement)
                updated_data = json.loads(updated_json_str)

                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(updated_data, file, indent=4)

                print(f"Remplacement effectué avec succès dans {filename}!")
    except Exception as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":

    images_folder = "images"
    metadata_folder = "metadata"

    IMAGES_FOLDER, METADATA_FOLDER = get_folder_path(images_folder, metadata_folder)

    image_extensions = (
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
    )  # Ajoutez d'autres extensions si besoin

    metadata_extensions = ".json"  # Ajoutez d'autres extensions si besoin

    images_cid = pin_folder_to_ipfs(
        images_folder,
        IMAGES_FOLDER,
        image_extensions,
    )

    replace_cid_in_json(METADATA_FOLDER, images_cid)

    CID = pin_folder_to_ipfs(
        metadata_folder,
        METADATA_FOLDER,
        metadata_extensions,
    )
