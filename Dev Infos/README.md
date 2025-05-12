# Guide d'information importante pour DEV

Ce document fournit des instructions détaillées pour configurer un environnement Python pour ce projet et gérer les versions de Python, les environnements virtuels, ainsi que les dépendances du projet.

---

## Configuration de l'Environnement Python

Suivez les étapes ci-dessous pour configurer votre environnement Python :

1. **Vérifier les versions de Python disponibles** :
   ```bash
   pyenv versions                  # Voir toutes les versions installées
   pyenv install --list            # Voir toutes les versions disponibles
   ```

2. **Installer et utiliser une version spécifique de Python** :
   ```bash
   pyenv install 3.10.12           # Installer une version spécifique
   pyenv local 3.10.12             # Utiliser cette version dans le projet
   ```

3. **Créer et activer un environnement virtuel** :
   ```bash
   python -m venv .venv            # Créer l’environnement virtuel
   source .venv/bin/activate       # Activer (Linux/macOS)
   .venv\Scripts\activate          # Activer (Windows)
   ```

4. **Désactiver et supprimer l'environnement virtuel** :
   ```bash
   deactivate                      # Désactiver l’environnement virtuel
   rm -r .venv                     # Supprimer le dossier .venv (Linux/macOS)
   rmdir /s /q .venv               # Supprimer le dossier .venv (Windows)
   ```

5. **Générer un fichier des dépendances** :
   ```bash
   pip freeze > requirements.txt   # Générer le fichier requirements.txt
   ```

---

## Cloner un Dépôt, le Modifier et le Pousser dans un Autre Dépôt

Cette section explique comment cloner un dépôt existant, y apporter des modifications, et pousser ces modifications dans un autre dépôt qui vous appartient.

### Étapes détaillées :

1. **Cloner le dépôt existant** :
   ```bash
   git clone <URL_DU_DEPOT_ORIGINAL> nom_du_dossier
   ```
   - Remplacez `<URL_DU_DEPOT_ORIGINAL>` par l'URL du dépôt que vous souhaitez cloner.
   - `nom_du_dossier` est le nom du dossier où le dépôt sera cloné.

2. **Se déplacer dans le dossier cloné** :
   ```bash
   cd nom_du_dossier
   ```

3. **Ajouter un nouveau dépôt distant (votre propre dépôt)** :
   - Supprimez l'ancien dépôt distant (optionnel) :
     ```bash
     git remote remove origin
     ```
   - Ajoutez votre dépôt comme distant :
     ```bash
     git remote add origin <URL_DE_VOTRE_DEPOT>
     ```
     Remplacez `<URL_DE_VOTRE_DEPOT>` par l'URL de votre dépôt personnel.

4. **Vérifier les dépôts distants** :
   ```bash
   git remote -v
   ```
   Cette commande affiche les dépôts distants configurés.

5. **Apporter vos modifications au projet** :
   - Modifiez les fichiers nécessaires dans le projet.

6. **Ajouter les modifications au suivi Git** :
   ```bash
   git add .
   ```

7. **Valider les modifications avec un message clair** :
   ```bash
   git commit -m "Votre message de commit"
   ```
   Remplacez `"Votre message de commit"` par un message décrivant vos modifications.

8. **Pousser les modifications dans votre dépôt** :
   ```bash
   git push -u origin main
   ```
   - Remplacez `main` par le nom de la branche par défaut de votre dépôt si ce n'est pas `main`.

---

### Remarques importantes :
- **URL des dépôts** : Assurez-vous de remplacer `<URL_DU_DEPOT_ORIGINAL>` et `<URL_DE_VOTRE_DEPOT>` par les URL correctes des dépôts GitHub ou autres.
- **Branche par défaut** : Si votre dépôt utilise une branche par défaut autre que `main`, adaptez les commandes en conséquence.
- **Gestion des conflits** : Si vous rencontrez des conflits lors du push, utilisez `git pull --rebase origin main` pour synchroniser les modifications avant de pousser.

---

Avec ces instructions détaillées, vous devriez être en mesure de cloner, modifier et pousser vos projets efficacement.
