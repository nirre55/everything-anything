from dotenv import load_dotenv
import os


def load_config():
    # Charge les variables d'environnement du fichier .env
    load_dotenv()

    # Récupère les clés
    jwk_key = os.getenv("PINATA_JWT")
    api_key = os.getenv("PINATA_API_KEY")
    api_secret_key = os.getenv("PINATA_SECRET_API_KEY")

    # Vérifie que toutes les clés sont présentes
    if not jwk_key or not api_key or not api_secret_key:
        raise ValueError("Une ou plusieurs clés manquent dans le fichier .env")

    # Retourne les clés sous forme de dictionnaire
    return {"jwk_key": jwk_key, "api_key": api_key, "api_secret_key": api_secret_key}


# Exemple d'utilisation
if __name__ == "__main__":
    config = load_config()
    print("Configuration chargée :", config)
