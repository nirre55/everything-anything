import json
import os

# Chemin du dossier contenant les fichiers JSON
dossier_json = r"C:\Users\Oulmi\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\Metadata\metadata"
# Chemin du fichier de sortie
fichier_sortie = r"C:\Users\Oulmi\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\Metadata\rarety-items\names.txt"

with open(fichier_sortie, "w") as f_out:
    # Parcourir tous les fichiers du dossier
    for fichier in os.listdir(dossier_json):
        if fichier.endswith(".json"):
            chemin_complet = os.path.join(dossier_json, fichier)

            try:
                with open(chemin_complet, "r") as f:
                    data = json.load(f)

                    # Extraire l'id
                    id_nft = data.get("id")

                    # Extraire le name (qui est dans attributes avec trait_type "Name")
                    name = None
                    for attr in data.get("attributes", []):
                        if attr.get("trait_type") == "Name":
                            name = attr.get("value")
                            break

                    if id_nft is not None and name is not None:
                        # Écrire la ligne formatée dans le fichier de sortie
                        ligne = (
                            f'{id_nft} => ManagedBuffer::new_from_bytes(b"{name}"),\n'
                        )
                        f_out.write(ligne)
                    else:
                        print(f"Champs manquants dans {fichier}")

            except Exception as e:
                print(f"Erreur avec le fichier {fichier}: {str(e)}")

print(f"Extraction terminée. Résultats dans {fichier_sortie}")
