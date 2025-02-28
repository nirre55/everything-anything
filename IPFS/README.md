# Uploader le répertoire sur IPFS local et Pin/Unpin avec Api Pinata

Ce guide explique comment uploader un répertoire sur un nœud IPFS local en utilisant la ligne de commande, puis pinner le CID généré sur Pinata avec un script Python.

## Pré-requis

1. **Nœud IPFS installé** :
   - Télécharge et installe IPFS depuis [ipfs.io](https://docs.ipfs.io/install/command-line/#install-official-binary-distributions) (par exemple, `kubo v0.15.0` ou plus récent).
   - Vérifie la version :
     ```bash
     ipfs version
     ```

2. **Python et dépendances** :
   - Installe Python 3.x.
   - Installe la bibliothèque `requests` :
     ```bash
     pip install requests
     ```
3. **Compte Pinata** :
   - Crée un compte sur [Pinata](https://pinata.cloud).
   - Récupère tes clés API (`PINATA_API_KEY` et `PINATA_SECRET_API_KEY`) depuis le tableau de bord.

## Uploader le répertoire sur IPFS local

1. **Structure du dossier** :
   - Prépare un dossier à uploader, par exemple :
     ```
     test_folder/
     ├── fichier1.txt
     └── fichier2.txt
     ```
2. **Lancer le daemon IPFS** :
   Ouvre un terminal et exécute :
   ```bash
   ipfs daemon
   ```

3. **Uploader le dossier** :
   Dans un autre terminal, utilise la commande suivante pour ajouter ton dossier à IPFS :
   ```bash
   ipfs add -r --cid-version=1 test_folder
   ```


## Supprimer/Unpin une image de pinata 

1. **Lancer le script unpin_pinata.py** :
   Ouvre un terminal et exécute :
   ```bash
   python script.py QmUBFTnx...