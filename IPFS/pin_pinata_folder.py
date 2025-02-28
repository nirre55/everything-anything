import requests
import json
import os
from pathlib import Path

# Remplacez par votre JWT Pinata
PINATA_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI1YzczYTQxOS02NmNhLTQwNzEtOTgyYS0yODUzMjI0NjI3ODEiLCJlbWFpbCI6ImRlc3RpbnluaXJyZUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJGUkExIn0seyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJOWUMxIn1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiOTFiYzI3ODZhMmQ2MWJhZjY2MTYiLCJzY29wZWRLZXlTZWNyZXQiOiJhMWZlMzFlMzgwMjYzYmMyY2E5NjU2NWRiMzVlNTQxY2VkZjkxZmFjZWNkYzE1MWQ2MDA2MWQ1OTcwMmFjMzJhIiwiZXhwIjoxNzcxODY0NDkwfQ.mH78AcaVaS83WeTIbNLss7JVrCcmzwEeo1Ef_1kW60A"
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


def generate_metadata(directory, cid, description, attributes):
    try:
        metadata_dir = os.path.join(os.path.dirname(directory), "metadata")
        os.makedirs(metadata_dir, exist_ok=True)

        image_extensions = (".png", ".jpg", ".jpeg", ".gif")

        for filename in os.listdir(directory):
            if filename.lower().endswith(image_extensions):
                file_id = os.path.splitext(filename)[0]
                metadata = {
                    "id": int(file_id),
                    "image": f"https://ipfs.io/ipfs/{cid}/{filename}",
                    "description": description,
                    "attributes": attributes,
                }

                metadata_file = os.path.join(metadata_dir, f"{file_id}.json")
                with open(metadata_file, "w", encoding="utf-8") as file:
                    json.dump(metadata, file, indent=4)

                print(f"Metadata générée pour {filename}!")
    except Exception as e:
        print(f"Erreur : {e}")


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
    # Liste des fichiers image dans le dossier local
    image_extensions = (
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
    )  # Ajoutez d'autres extensions si besoin

    images_cid = pin_folder_to_ipfs(
        "images",
        r"C:\Users\Oulmi\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\images",
        image_extensions,
    )

    generate_metadata(
        r"C:\Users\Oulmi\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\images",
        images_cid,
        "my nft collection description",
        [{"trait_type": "Country", "value": "France"}],
    )

    metadata_extensions = ".json"  # Ajoutez d'autres extensions si besoin

    CID = pin_folder_to_ipfs(
        "metadatas",
        r"C:\Users\Oulmi\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\metadata",
        metadata_extensions,
    )
