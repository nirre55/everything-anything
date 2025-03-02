# Uploader le répertoire sur IPFS local et Pin/Unpin avec Api Pinata

Ce guide explique comment uploader un répertoire sur un nœud IPFS local en utilisant la ligne de commande, puis pinner le CID généré sur Pinata avec un script Python.

## 📌 Sommaire
- [Pré-requis](#pré-requis)
- [Uploader le répertoire sur IPFS local](#uploader-le-répertoire-sur-ipfs-local)
- [Pin avec Cid](#pin-un-fichierfolder-dans-pinata-avec-cid)
- [Unpin image sur pinata](#supprimerunpin-une-image-de-pinata)
- [Upload un folder dans pinata](#upload-un-folder-dans-pinata)
- [Upload un fichier dans pinata](#upload-un-fichier-dans-pinata)

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

**Commande utiles** 

- **Lister tous les pins (CID pinnés localement)** 
    ```bash
    ipfs pin ls
    ```

- **Suppression** 
    ```bash
    ipfs pin ls
    ```
        
- **Nettoyage**
    ```bash
    ipfs repo gc
    ```

**Remarques importantes**

- **Pins indirects :** Vous ne pouvez pas supprimer directement un pin indirect avec `ipfs pin rm`. Il faut supprimer le pin récursif qui le référence.

- **Pinata :** Supprimer un pin local n'affecte pas Pinata. Si le CID est aussi épinglé sur Pinata, il restera disponible via leur passerelle (`https://ipfs.io/ipfs/<CID>`). Pour le supprimer de Pinata, utilisez leur API ou l'interface web.

- **Erreur "pinned indirectly" :**
  - Si vous obtenez :
    ```
    Error: pin: cid was pinned indirectly: On...
    ```
    Cela signifie que le CID est un enfant d'un pin récursif. Trouvez le CID parent avec `ipfs pin ls --type=recursive` et supprimez-le.


## Pin un fichier/folder dans pinata avec CID 

1. **Pré-requis** :
   - Upload en local

2. **Lancer le script pin_pinata_with_cid.py** :
   - Modifier cette ligne de code pour mettre le bon CID :
    ```python
    if __name__ == "__main__":
        pin_cid_to_pinata("bafkreid2ek6qmbdfmtza2zo2rjwoopmw3attszoeif")
        
**Remarques importantes**

- Ce n'est pas encore testé car il faudrait un plan payant (Pinata)
    ```
    Erreur lors du pinning : 403 Client Error: Forbidden for url: https://api.pinata.cloud/pinning/pinHashToIPFS

    Réponse de l'API : {"error":{"reason":"PAID_FEATURE_ONLY","details":"You must be on a paid plan to pin by CID"}}
    ```

## Supprimer/Unpin une image de pinata 

1. **Lancer le script unpin_pinata.py** :

   - Ouvre un terminal et exécute :
   ```bash
   python script.py QmUBFTnx...

## Upload un folder dans pinata 

1. **Pré-requis** :
   - Preparer le dossier a upload dans notre exemple : images
   - Modifier les paths les extentions au besoin et metadata (description et attributs):
   ```python
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
        r"C:\Users\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\images",
        image_extensions,
    )

    generate_metadata(
        r"C:\Users\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\images",
        images_cid,
        "my nft collection description",
        [{"trait_type": "Country", "value": "France"}],
    )

    metadata_extensions = ".json"  # Ajoutez d'autres extensions si besoin

    CID = pin_folder_to_ipfs(
        "metadatas",
        r"C:\Users\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\metadata",
        metadata_extensions,
    )

2. **Lancer le script pin_pinata_folder.py** :

   - Ouvre un terminal et exécute :
   ```bash
   python pin_pinata_folder.py 

## Upload un file dans pinata 

1. **Pré-requis** :
   - Preparer le fichier a upload dans notre exemple : 2.png
   - Modifier les paths et metadata (description et attributs):
   ```python
    if __name__ == "__main__":
        image_path = r"C:\Users\OneDrive\Bureau\Python Project\Everything-Anything\IPFS\images\2.png"
        description = "my nft collection description"
        attributes = [{"trait_type": "Country", "value": "France"}]
        retour = upload_single_to_ipfs(image_path, description, attributes)
        print(retour)


2. **Lancer le script pin_pinata_file.py** :

   - Ouvre un terminal et exécute :
   ```bash
   python pin_pinata_file.py 