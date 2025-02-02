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

---

## 1. Probabilités fixes (RNG - Random Number Generation)
**Description** : Chaque objet a une probabilité fixe d'être obtenu après un événement spécifique (ex : vaincre un ennemi).  
**Exemple** : Un boss a 10 % de chance de lâcher une épée rare et 2 % pour une armure légendaire.  
**Avantages** : Simple à implémenter, crée un sentiment d'excitation.  
**Inconvénients** : Peut frustrer les joueurs malchanceux.

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

## Conclusion
Chaque technique de drop a ses avantages et ses inconvénients. Le choix dépend du design du jeu, de l'expérience souhaitée pour les joueurs et des contraintes techniques. Une combinaison de plusieurs techniques est souvent utilisée pour créer un système de loot équilibré et engageant.


