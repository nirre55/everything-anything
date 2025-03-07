# Systèmes de Loot dans les Jeux Vidéo

Ce dépôt documente les différentes méthodes de drop et de loot utilisées dans les jeux vidéo. Il inclut des descriptions détaillées, des exemples d'utilisation et les avantages/inconvénients de chaque approche.

## 📌 Sommaire
- [1. Probabilités Fixes (RNG)](#1-probabilités-fixes-rng)
- [2. Tables de Loot](#2-tables-de-loot)
- [3. Systèmes de Protection Contre la Malchance (Pity System)](#3-systèmes-de-protection-contre-la-malchance-pity-system)
- [4. Drops Conditionnels](#4-drops-conditionnels)
- [5. Systèmes de Graines (Seed-based RNG)](#5-systèmes-de-graines-seed-based-rng)
- [6. Drops Dynamiques (Scaling Loot)](#6-drops-dynamiques-scaling-loot)
- [7. Drops Garantis](#7-drops-garantis)
- [8. Systèmes de Crafting ou d'Échange](#8-systèmes-de-crafting-ou-déchange)
- [9. Drops Basés sur la Contribution du Joueur](#9-drops-basés-sur-la-contribution-du-joueur)
- [10. Systèmes de Saison ou de Rotation](#10-systèmes-de-saison-ou-de-rotation)
- [11. Drops Communautaires (Shared Loot)](#11-drops-communautaires-shared-loot)
- [12. Drops Basés sur la Localisation](#12-drops-basés-sur-la-localisation)
- [13. Systèmes de Tokenisation](#13-systèmes-de-tokenisation)
- [14. Systèmes de Loot Évolutif](#14-systèmes-de-loot-évolutif)
- [15. Systèmes de Loot Négociable](#15-systèmes-de-loot-négociable)
- [16. Wow Drop Loot ](#16-wow_drop_loot)
---

## 1. Probabilités fixes (RNG - Random Number Generation)
**Description** : Chaque objet a une probabilité fixe d'être obtenu après un événement spécifique (ex : vaincre un ennemi).  
**Exemple** : Un boss a 10 % de chance de lâcher une épée rare et 2 % pour une armure légendaire.  
**Avantages** : Simple à implémenter, crée un sentiment d'excitation.  
**Inconvénients** : Peut frustrer les joueurs malchanceux.

## Script: fixed_probability.py
Ce script simule le système de loot d'un jeu, où un joueur a la possibilité d'obtenir une épée rare, une armure légendaire ou rien du tout après avoir vaincu un boss.

### 1. Probabilités de Loot

- **Épée rare** : `10%` de chance d'obtention.
- **Armure légendaire** : `2%` de chance d'obtention.
- **Rien** : `88%` de chance de ne rien obtenir.

### 2. Fonctionnement du Script

1. **Génération d'un Nombre Aléatoire**  
   Le script utilise `random.random()` pour générer un nombre flottant entre `0` et `1`.

2. **Détermination du Loot**  
   - Si le nombre généré est inférieur à `0.02` (`2%`), le joueur obtient une **armure légendaire**.
   - Sinon, si le nombre est inférieur à `0.12` (`2% + 10%`), le joueur obtient une **épée rare**.
   - Sinon, le joueur **n'obtient rien**.

3. **Simulation de Plusieurs Défaites**  
   La fonction `simulate_boss_defeats` permet de simuler la défaite du boss un certain nombre de fois et de compter les résultats obtenus.

4. **Affichage des Résultats**  
   Après la simulation, le script affiche :
   - Le nombre de fois que chaque objet a été obtenu.
   - Le pourcentage correspondant par rapport au nombre total de simulations.

## Utilisation

Pour utiliser ce script, assurez-vous d'avoir **Python** installé sur votre machine. Exécutez le script et spécifiez le **nombre de simulations** souhaitées. Le script affichera alors les résultats détaillés de la simulation.

### Exemple de Résultats

Après avoir simulé `10 000` défaites du boss, les résultats pourraient être les suivants :

```plaintext
Armures légendaires obtenues : 200 (2%)
Épées rares obtenues : 1 000 (10%)
Aucun loot : 8 800 (88%)
```

---

## 2. Tables de loot (Loot Tables)
**Description** : Les objets sont regroupés dans une table avec des probabilités spécifiques.  
**Exemple** : Un boss peut avoir une table avec 50 % de chance de donner une potion, 30 % pour une armure et 20 % pour une arme.  
**Avantages** : Permet un meilleur contrôle sur les drops.  
**Inconvénients** : Nécessite un équilibrage minutieux.

---

## 3. Systèmes de protection contre la malchance (Pity System)
**Description** : Si un joueur échoue plusieurs fois à obtenir un objet rare, ses chances augmentent progressivement ou il est garanti de l'obtenir après un certain nombre d'essais.  
**Exemple** : Dans les jeux de gacha, un joueur est assuré d'obtenir un personnage rare après 100 tirages.  
**Avantages** : Réduit la frustration des joueurs malchanceux.  
**Inconvénients** : Peut diminuer l'excitation de l'aléatoire.

---

## 4. Drops conditionnels
**Description** : Certains objets ne sont obtenus que si des conditions spécifiques sont remplies.  
**Exemple** : Un boss ne lâche une épée légendaire que si le joueur le bat en moins de 2 minutes.  
**Avantages** : Encourage des stratégies variées et récompense la maîtrise.  
**Inconvénients** : Peut frustrer les joueurs qui ne remplissent pas les conditions.

---

## 5. Systèmes de graines (Seed-based RNG)
**Description** : L'aléatoire est basé sur une graine (seed) spécifique, rendant les résultats reproductibles.  
**Exemple** : Dans Minecraft, la graine du monde détermine la génération des ressources et des coffres.  
**Avantages** : Permet aux joueurs de partager des expériences spécifiques.  
**Inconvénients** : Moins adapté aux jeux où l'aléatoire pur est recherché.

---

## 6. Drops dynamiques (Scaling Loot)
**Description** : Les objets qui tombent sont ajustés en fonction du niveau du joueur, de la difficulté ou d'autres paramètres.  
**Exemple** : Dans "Diablo", un monstre de haut niveau lâche de meilleurs objets qu'un monstre bas niveau.  
**Avantages** : Garde le loot pertinent tout au long de la progression du joueur.  
**Inconvénients** : Peut rendre les objets trop prévisibles.

---

## 7. Drops garantis (Guaranteed Drops)
**Description** : Certains ennemis ou coffres donnent toujours un objet précis.  
**Exemple** : Un boss lâche toujours une clé nécessaire pour avancer dans l’histoire.  
**Avantages** : Utile pour les objets essentiels à la progression.  
**Inconvénients** : Moins excitant que l’aléatoire.

---

## 8. Systèmes de crafting ou d'échange
**Description** : Les joueurs collectent des ressources au lieu de loots directs, puis les utilisent pour fabriquer ou échanger des objets.  
**Exemple** : Dans "Monster Hunter", les joueurs récoltent des matériaux pour forger des armes et armures.  
**Avantages** : Encourage l'exploration et la planification.  
**Inconvénients** : Peut être fastidieux pour certains joueurs.

---

## 9. Drops basés sur la contribution du joueur
**Description** : La probabilité d'obtenir un objet dépend de la participation du joueur (ex : dégâts infligés, soins prodigués).  
**Exemple** : Dans certains MMORPG, les joueurs qui infligent plus de dégâts ont plus de chances d'obtenir un loot rare.  
**Avantages** : Récompense l'investissement et la performance.  
**Inconvénients** : Peut désavantager les joueurs moins expérimentés.

---

## 10. Systèmes de saison ou de rotation
**Description** : Les objets disponibles changent en fonction du temps (événements saisonniers, cycles de rotation).  
**Exemple** : Dans "Fortnite", certains skins et objets ne sont disponibles que pendant un événement spécial.  
**Avantages** : Crée un sentiment d’urgence et de rareté.  
**Inconvénients** : Peut frustrer les joueurs qui manquent une occasion.

---

## 11. Drops communautaires (Shared Loot)
**Description** : Les objets sont partagés entre plusieurs joueurs, soit de manière équitable, soit via un système de priorité.  
**Exemple** : Dans les MMORPG, certains objets nécessitent un "jet de dés" pour être attribués à un joueur du groupe.  
**Avantages** : Encourage la coopération et l'entraide.  
**Inconvénients** : Peut créer des tensions entre les joueurs.

---

## 12. Drops basés sur la localisation
**Description** : Le type d’objets obtenus dépend de l’endroit où l’ennemi est vaincu ou du coffre ouvert.  
**Exemple** : Dans "The Legend of Zelda", certains coffres contiennent toujours les mêmes objets à un emplacement précis.  
**Avantages** : Encourage l’exploration et la découverte.  
**Inconvénients** : Peut limiter la diversité des loots si trop rigide.

---

## 13. Systèmes de tokenisation
**Description** : Au lieu d’obtenir directement un objet rare, les joueurs reçoivent des jetons échangeables contre des objets de leur choix.  
**Exemple** : Après chaque boss, les joueurs reçoivent des fragments qui permettent d’acheter un objet rare spécifique.  
**Avantages** : Réduit l’aléatoire et donne un objectif clair aux joueurs.  
**Inconvénients** : Moins excitant qu’un drop spontané.

---

## 14. Systèmes de loot évolutif
**Description** : Plus un joueur affronte un boss, plus les drops évoluent ou changent.  
**Exemple** : Un boss lâche un premier loot standard, mais si le joueur le bat plusieurs fois, de nouveaux objets plus puissants deviennent disponibles.  
**Avantages** : Encourage la rejouabilité et la persévérance.  
**Inconvénients** : Peut créer une routine répétitive.

---

## 15. Systèmes de loot négociable
**Description** : Les objets obtenus peuvent être échangés ou vendus entre joueurs.  
**Exemple** : Dans "World of Warcraft", certains loots sont échangeables entre membres d’un raid pendant un temps limité.  
**Avantages** : Permet aux joueurs d’obtenir ce dont ils ont besoin sans dépendre de la chance pure.  
**Inconvénients** : Peut favoriser l’exploitation et l'économie parallèle (marché noir).

---

## 16. Wow Drop Loot 

### Description :
`wow_drop_loot.py` est un script Python qui simule un système de loot (butin) inspiré des jeux de type RPG, comme World of Warcraft. Il génère une liste d'objets avec des raretés et probabilités associées, effectue des simulations de drops, et produit des statistiques détaillées. Les probabilités sont sauvegardées pour garantir une cohérence entre les exécutions.

Le script utilise des catégories de rareté (Commun, Peu commun, Rare, Épique, Légendaire) avec des proportions prédéfinies et attribue des probabilités spécifiques à chaque objet en fonction de sa rareté.

### Fonctionnalités principales :
- **Génération d'objets** : Crée une liste de `NOMBRE_ELEMENTS` objets (par défaut 259), numérotés de "1" à "259", mélangés aléatoirement.
- **Répartition des raretés** : Assigne des raretés selon les proportions suivantes :
  - Commun : 40 %
  - Peu commun : 30 %
  - Rare : 20 %
  - Épique : 9 %
  - Légendaire : 1 %
- **Probabilités** : Attribue une probabilité à chaque objet dans une plage spécifique à sa rareté :
  - Commun : 20 % à 40 %
  - Peu commun : 10 % à 19 %
  - Rare : 5 % à 9 %
  - Épique : 1 % à 4 %
  - Légendaire : 0.1 % à 0.9 %
- **Simulation de drops** : Génère des drops avec un minimum de 3 objets (`MIN_ITEMS`) et un maximum de 5 (`MAX_ITEMS`) par simulation, en respectant les probabilités.
- **Statistiques** : Calcule les occurrences et pourcentages par objet et par rareté après `NUM_SIMULATIONS` (par défaut 1000).
- **Sauvegarde/Chargement** : Sauvegarde les probabilités et raretés dans un fichier pour une réutilisation cohérente.

### Fichiers générés :
Le script crée deux fichiers dans le même dossier que `wow_drop_loot.py` :
1. **`loot_simulation_results.txt`** :
   - Contient les probabilités initiales, les résultats des simulations, et les statistiques.
   - Exemple de contenu :
     ```
     Probabilités attribuées aux objets :
     45 (Commun): 25.67%
     123 (Rare): 7.89%
     ...

     Résultats des 1000 simulations :
     Simulation 1 : ['45', '123', '7']
     ...

     Statistiques après 1000 simulations :
     45 (Commun): 250 fois (5.00% des drops possibles, probabilité initiale: 25.67%)
     ...

     Statistiques par rareté :
     Commun: 2000 fois (40.12% des drops totaux)
     ...
     ```
2. **`probabilities.txt`** :
   - Fichier JSON stockant la liste des items, leurs probabilités et raretés.
   - Généré à la première exécution, chargé aux exécutions suivantes.
   - Exemple :
     ```json
     {
         "items": ["45", "123", "7", ...],
         "probs": {"45": 25.67, "123": 7.89, ...},
         "rarities": {"45": "Commun", "123": "Rare", ...}
     }
     ```

---

## Conclusion
Chaque technique de drop a ses avantages et ses inconvénients. Le choix dépend du design du jeu, de l'expérience souhaitée pour les joueurs et des contraintes techniques. Une combinaison de plusieurs techniques est souvent utilisée pour créer un système de loot équilibré et engageant.


