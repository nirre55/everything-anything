import requests
import os
import json
import os
from Utils.env_loader import load_env

# Charge les variables d'environnement
load_env()


# Vos clés API Pinata
PINATA_API_KEY = os.getenv("api_key")
PINATA_SECRET_API_KEY = os.getenv("api_secret_key")

PINATA_API_URL = "https://api.pinata.cloud"

# Headers de base pour l'authentification
headers = {
    "pinata_api_key": PINATA_API_KEY,
    "pinata_secret_api_key": PINATA_SECRET_API_KEY,
}


def upload_file(file_path):
    """Upload un fichier sur IPFS via Pinata"""
    try:
        url = f"{PINATA_API_URL}/pinning/pinFileToIPFS"
        file = {"file": (os.path.basename(file_path), open(file_path, "rb"))}

        response = requests.post(url, headers=headers, files=file)
        response.raise_for_status()

        ipfs_hash = response.json()["IpfsHash"]
        return f"https://ipfs.io/ipfs/{ipfs_hash}"

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'upload de du fichier {file_path}: {e}")
        raise


def generate_metadata(file_path, image_url, description, attributes):
    try:
        if not os.path.isfile(file_path):
            print("Erreur : fichier introuvable.")
            return

        metadata_dir = os.path.join(
            os.path.dirname(os.path.dirname(file_path)), "metadata"
        )
        os.makedirs(metadata_dir, exist_ok=True)

        filename = os.path.basename(file_path)
        file_id, ext = os.path.splitext(filename)
        image_extensions = (".png", ".jpg", ".jpeg", ".gif")

        if ext.lower() not in image_extensions:
            print("Erreur : format de fichier non supporté.")
            return

        metadata = {
            "id": int(file_id),
            "image": image_url,
            "description": description,
            "attributes": attributes,
        }

        metadata_file = os.path.join(metadata_dir, f"{file_id}.json")
        with open(metadata_file, "w", encoding="utf-8") as file:
            json.dump(metadata, file, indent=4)

        print(f"Metadata générée pour {filename}!")
        return metadata_file
    except Exception as e:
        print(f"Erreur : {e}")
        return None


def upload_single_to_ipfs(image_path, description, attributes):
    """Upload une image et ses métadonnées sur IPFS"""
    try:
        # 1. Upload de l'image
        image_url = upload_file(image_path)

        # 2. Création des métadonnées
        metadata_path = generate_metadata(
            image_path, image_url, description, attributes
        )

        # 3. Upload des métadonnées
        metadata_url = upload_file(metadata_path)

        return {"image_url": image_url, "metadata_url": metadata_url}

    except Exception as e:
        print(f"Erreur dans le processus d'upload pour {image_path}: {e}")
        return None


# Exemple d'utilisation
if __name__ == "__main__":
    image_path = r""  # image path here
    description = "my nft collection description"
    attributes = [{"trait_type": "Country", "value": "France"}]
    retour = upload_single_to_ipfs(image_path, description, attributes)
    print(retour)
