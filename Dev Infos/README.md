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
