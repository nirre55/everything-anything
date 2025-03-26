# **Everything and Anything** 🎪

Bienvenue dans **Everything and Anything**, le repo ultime où le chaos rencontre la créativité ! C'est l'endroit où des scripts aléatoires, des expériences folles et des bouts de code en vrac prennent vie. Attends-toi à l'inattendu, car ici, **tout est possible et n'importe quoi peut arriver** ! 🚀

---

# 📦 Installation et Structure du Projet

Ce document explique l'utilisation du fichier `setup.py`, la commande d'installation, ainsi que l'importance du fichier `__init__.py` pour rendre les modules importables.

---

## Le fichier `setup.py`
Le fichier `setup.py` est utilisé pour transformer le projet en **package installable**. Cela permet d'importer ses modules sans ajouter `sys.path` manuellement dans chaque script.

## Installation du package
Après avoir cloné le projet, exécutez la commande suivante à la racine du projet :
```sh
pip install -e .
```
1. **Explication** :

    - pip install -e . (mode editable) permet d'utiliser le package sans devoir le réinstaller après chaque modification.

    - Une fois installé, les modules du projet peuvent être importés sans manipulation de sys.path.

2. **Automatisation** :
Vous pouvez aussi créer un script d’installation :

    - Windows : install.bat

    - Linux/macOS : install.sh

## Quand ajouter __init__.py ?
Le fichier __init__.py est nécessaire dans chaque dossier contenant des modules Python pour que ceux-ci soient reconnus comme des packages.

1. **Où ajouter __init__.py ?**
    - Obligatoire dans les dossiers contenant du code réutilisable 

2. **Cas où __init__.py n’est pas nécessaire**

    - Si le dossier ne contient que des scripts exécutables (scripts/).

    - Si le dossier ne doit pas être importé comme module.
