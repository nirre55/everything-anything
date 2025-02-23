import os
import json
import requests
from pathlib import Path

# Configuration Pinata
PINATA_API_KEY = "ton_api_key"
PINATA_SECRET = "ton_secret_key"
PINATA_URL = "https://api.pinata.cloud/pinning/pinFileToIPFS"
HEADERS = {
    "pinata_api_key": PINATA_API_KEY,
    "pinata_secret_api_key": PINATA_SECRET,
}

IMAGE_FOLDER = "images"
METADATA_FOLDER = "metadata"
Path(METADATA_FOLDER).mkdir(exist_ok=True)

# Fonction pour uploader un dossier sur Pinata et récupérer le CID
def upload_folder_to_pinata(folder_path):
    files = []
    for root, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(("file", (os.path.relpath(file_path, folder_path), open(file_path, "rb"))))
    
    response = requests.post(PINATA_URL, headers=HEADERS, files=files)
    if response.status_code == 200:
        cid = response.json()["IpfsHash"]
        return cid  # Retourne uniquement le CID
    else:
        raise Exception(f"Erreur lors de l'upload : {response.text}")

# Générer les métadonnées avec un CID commun pour les images
def generate_metadata(image_base_cid, token_id, country_name):
    metadata = {
        "name": f"World Border NFT #{token_id}",
        "description": "Un NFT représentant une bordure de pays sur MultiversX.",
        "image": f"https://ipfs.io/ipfs/{image_base_cid}/{country_name}.png",  # Lien avec ipfs.io
        "attributes": [
            {"trait_type": "Token ID", "value": str(token_id)},
            {"trait_type": "Country", "value": country_name},
            {"trait_type": "Blockchain", "value": "MultiversX"}
        ],
        "tags": ["multiversx", "nft", "worldmap"],
        "nonce": token_id
    }
    
    metadata_path = f"{METADATA_FOLDER}/{token_id}.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

# Traitement
def process_collection():
    # Uploader le dossier des images
    print("Upload du dossier images...")
    image_base_cid = upload_folder_to_pinata(IMAGE_FOLDER)
    image_base_url = f"https://ipfs.io/ipfs/{image_base_cid}"
    print(f"CID des images : {image_base_cid}")
    print(f"Base URL des images : {image_base_url}")
    
    # Générer les métadonnées
    token_id = 0
    for image_file in sorted(os.listdir(IMAGE_FOLDER)):
        if image_file.endswith((".png", ".jpg", ".jpeg")):
            country_name = os.path.splitext(image_file)[0]
            generate_metadata(image_base_cid, token_id, country_name)
            token_id += 1
    
    # Uploader le dossier des métadonnées
    print("Upload du dossier metadata...")
    metadata_base_cid = upload_folder_to_pinata(METADATA_FOLDER)
    metadata_base_url = f"https://ipfs.io/ipfs/{metadata_base_cid}"
    print(f"CID des métadonnées : {metadata_base_cid}")
    print(f"Base URL des métadonnées : {metadata_base_url}")
    
    # Sauvegarder les résultats
    with open("output/nft_urls.json", "w") as f:
        json.dump({
            "image_base_url": image_base_url,
            "image_cid": image_base_cid,
            "metadata_base_url": metadata_base_url,
            "metadata_cid": metadata_base_cid
        }, f, indent=4)
    print("Résultats sauvegardés dans output/nft_urls.json")

if __name__ == "__main__":
    process_collection()