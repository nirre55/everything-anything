import requests
import sys
from load_config import load_config

# Charge les variables d'environnement
config = load_config()


# Vos clés API Pinata
PINATA_API_KEY = config["api_key"]
PINATA_SECRET_API_KEY = config["api_secret_key"]

UNPIN_URL = "https://api.pinata.cloud/pinning/unpin/"
HEADERS = {
    "pinata_api_key": PINATA_API_KEY,
    "pinata_secret_api_key": PINATA_SECRET_API_KEY,
}


# Fonction pour unpin un CID de Pinata
def unpin_from_pinata(cid):
    try:
        response = requests.delete(f"{UNPIN_URL}{cid}", headers=HEADERS)
        if response.status_code == 200:
            print(f"CID {cid} a été unpinned avec succès. Espace libéré.")
        else:
            raise Exception(
                f"Erreur lors de l'unpin : {response.status_code} - {response.text}"
            )
    except Exception as e:
        print(f"Erreur : {str(e)}")


# Vérification et exécution
if __name__ == "__main__":
    # Vérifier si un CID est passé en argument
    if len(sys.argv) != 2:
        print("Usage : python script.py <CID>")
        print("Exemple : python script.py QmUBFTnx...")
        sys.exit(1)

    cid = sys.argv[1]
    print(f"Tentative de suppression du CID : {cid}")
    unpin_from_pinata(cid)
