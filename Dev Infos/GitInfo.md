1. Cloner, modifier et pousser dans un autre dépôt
2. Synchroniser un dépôt avec l’état local (y compris les suppressions)

---

# 📘 Guide Git : Clonage, Modification et Synchronisation d'un Dépôt

Ce guide contient deux parties :

1. Cloner un dépôt existant, le modifier, et pousser vers un autre dépôt.
2. Synchroniser un dépôt distant avec les fichiers locaux, y compris les suppressions.

---

## 🔄 1. Cloner un Dépôt, le Modifier et le Pousser vers un Autre Dépôt

Cette section explique comment cloner un dépôt Git, y apporter des modifications, puis pousser ces changements dans **votre propre dépôt distant**.

---

### ✅ Étapes à suivre

#### 1. Cloner le dépôt d’origine

```bash
git clone <URL_DU_DEPOT_ORIGINAL> nom_du_dossier
```

- Remplacez `<URL_DU_DEPOT_ORIGINAL>` par l’URL du dépôt que vous souhaitez cloner.
- `nom_du_dossier` est le nom du dossier local dans lequel le dépôt sera cloné.

---

#### 2. Se déplacer dans le dossier cloné

```bash
cd nom_du_dossier
```

---

#### 3. Remplacer l’origine par votre propre dépôt

##### a. Supprimer l’ancien dépôt distant (optionnel)

```bash
git remote remove origin
```

##### b. Ajouter votre propre dépôt distant

```bash
git remote add origin <URL_DE_VOTRE_DEPOT>
```

- Remplacez `<URL_DE_VOTRE_DEPOT>` par l’URL de votre dépôt personnel.

---

#### 4. Vérifier la configuration des dépôts distants

```bash
git remote -v
```

Vous devriez voir votre propre dépôt listé sous `origin`.

---

#### 5. Apporter vos modifications

- Modifiez les fichiers nécessaires dans le projet.
- Ajoutez, modifiez ou supprimez des fichiers selon vos besoins.

---

#### 6. Ajouter tous les changements (ajouts, modifs, suppressions)

```bash
git add -A
```

---

#### 7. Faire un commit avec un message clair

```bash
git commit -m "Votre message de commit"
```

---

#### 8. Pousser vers votre propre dépôt

```bash
git push -u origin main
```

> Remplacez `main` si votre branche principale porte un autre nom (`master`, `develop`, etc.).

---

### 📝 Remarques

- 🔗 **URLs à adapter** : Utilisez les bonnes adresses de dépôts Git.
- 🌿 **Nom de branche** : Adaptez `main` si nécessaire.
- ⚠️ **En cas de conflit** :

  ```bash
  git pull --rebase origin main
  ```

---

## 🧹 2. Synchroniser un Dépôt avec les Fichiers Locaux (y compris les suppressions)

Cette section vous explique comment faire en sorte que le dépôt distant reflète **exactement** l’état de vos fichiers locaux, même si vous avez **supprimé des fichiers ou des dossiers**.

---

### ✅ Étapes à suivre

#### 1. Ouvrir un terminal dans le dossier du projet

```bash
cd /chemin/vers/mon/projet
```

---

#### 2. Vérifier les changements détectés par Git

```bash
git status
```

Vous verrez les fichiers modifiés, ajoutés ou supprimés.

---

#### 3. Ajouter **tous** les changements à Git (y compris les suppressions)

```bash
git add -A
```

> `-A` permet d’inclure toutes les modifications : ajouts, suppressions, modifications.

---

#### 4. Valider les changements

```bash
git commit -m "Suppression de fichiers obsolètes et mise à jour"
```

---

#### 5. Pousser vers le dépôt distant

```bash
git push origin main
```

> Remplacez `main` par la branche utilisée dans votre dépôt.

---

### 🧪 Vérification

Après avoir poussé, vous pouvez exécuter :

```bash
git fetch
git status
```

Si vous voyez `Your branch is up to date with 'origin/main'`, tout est bien synchronisé ✅

---

## 📝 Remarques

- 🗑️ Les fichiers supprimés localement ne disparaîtront du dépôt distant **que si** vous les ajoutez au commit avec `git add -A`.
- 🧭 Si des fichiers apparaissent encore sur GitHub, vérifiez que :

  - Vous avez bien commité les suppressions.
  - Vous avez bien fait un `git push`.

---
