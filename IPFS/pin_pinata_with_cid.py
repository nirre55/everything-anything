import requests
import json

# Configuration Pinata
PINATA_API_KEY = "91bc2786a2d61baf6616"
PINATA_SECRET_API_KEY = (
    "a1fe31e380263bc2ca96565db35e541cedf91facecdc151d60061d59702ac32a"
)
PINATA_API_URL = "https://api.pinata.cloud/pinning/pinHashToIPFS"


def pin_cid_to_pinata(cid):
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY,
    }
    payload = {"hashToPin": cid, "pinataOptions": json.dumps({"cidVersion": 1})}
    try:
        response = requests.post(PINATA_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        print(f"CID {cid} pinné sur Pinata avec succès !")
        print(f"Détails : {result}")
        return result
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du pinning : {str(e)}")
        print(f"Réponse de l'API : {e.response.text}")
        return None


if __name__ == "__main__":
    pin_cid_to_pinata("bafkreid2ek6qmbdfmtza2zo2rjwoopmw3attszoeif6yltsdj5mucp7nre")
