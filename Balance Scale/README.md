# 🎉 Balance Scale 🎉

**Règles du Jeu:**

- **Choisissez un Nombre** 📊: Chaque joueur doit choisir un nombre entre **0 et 100**.
  
- **Calcul du Nombre Gagnant** 🧮: La **moyenne** des nombres choisis par tous les joueurs sera multipliée par **0,8**. Ce produit sera le **nombre gagnant**.

- **Gagner la Manche** 🏆: Le joueur qui **devine le nombre gagnant** ou celui qui est le **plus proche** remporte la manche. 

- **Points Négatifs** 😢: Tous les joueurs, sauf le gagnant, **reçoivent un point négatif** à chaque manche.

- **Fin de Partie** 🚫: Lorsqu'un joueur atteint **dix points négatifs**, la partie est **terminée pour lui** avec un 'GAME OVER'.

- **Nouvelle Règle** 📜: À chaque 'GAME OVER', **une nouvelle règle sera ajoutée** au jeu.

- **Début de Partie** 🔄: Tous les joueurs commencent avec un **score de zéro**.

---

## **Balance Scale : Stratégie et Analyse**

Le jeu **Balance Scale** est un jeu stratégique où les joueurs doivent anticiper les choix des autres pour minimiser leurs points négatifs. Voici une analyse détaillée et des conseils pour optimiser vos chances de gagner :

### **Mécanismes Clés :**
1. **Nombre Gagnant :** Moyenne des nombres choisis × 0,8.
2. **Élimination :** 10 points négatifs = **GAME OVER**, avec une nouvelle règle ajoutée à chaque élimination.
3. **Stratégie Dynamique :** Les règles évoluent au fil des éliminations, nécessitant une adaptation constante.

---

### **Stratégie de Base :**
1. **Équilibre de Nash Théorique :**
   - Si tous les joueurs sont parfaitement rationnels, le nombre optimal tend vers **0** (car \(0,8^n \times 100 \rightarrow 0\) après \(n\) itérations). Mais en pratique, les joueurs s'arrêtent à quelques niveaux de raisonnement.

2. **Niveaux de Pensée (Théorie des Jeux) :**
   - **Niveau 0 :** Choix aléatoire (ex: 50).
   - **Niveau 1 :** Suppose que la moyenne est 50 → choisit \(50 \times 0,8 = 40\).
   - **Niveau 2 :** Suppose que d'autres pensent comme niveau 1 → choisit \(40 \times 0,8 = 32\).
   - **Niveau k :** \(100 \times (0,8)^k\). Adaptez \(k\) selon le groupe (débutants vs experts).

3. **Adaptation aux Règles Dynamiques :**
   - Après chaque élimination, une nouvelle règle est introduite (ex: multiplicateur ajusté, pénalités, etc.). Soyez prêt à recalculer votre stratégie.

---

### **Conseils Pratiques :**
1. **Première Manche :**
   - Si le groupe est inexpérimenté, visez **32–40** (niveau 2-3). Pour des experts, descendez vers **10–20**.

2. **Analyser les Résultats Passés :**
   - Si le nombre gagnant diminue régulièrement, anticipez une poursuite de la tendance (ex: 50 → 40 → 32 → ...).

3. **Gestion des Points Négatifs :**
   - Si vous approchez de 10 points, jouez plus prudemment (choisissez des nombres proches des précédents gagnants).

4. **Nouvelles Règles :**
   - Si une règle avantage les petits nombres (ex: multiplicateur réduit à 0,7), descendez davantage. Si elle pénalise les extrêmes, restez au centre.

---

### **Exemple de Simulation :**
- **Manche 1 :** Tous choisissent 50 → Gagnant = \(50 \times 0,8 = 40\).
- **Manche 2 :** Les joueurs visent 40 → Gagnant = \(32\).
- **Manche 3 :** Stratèges avancés choisissent 25 → Gagnant = \(20\).
- **Élimination :** Un joueur atteint 10 points → Nouvelle règle (ex: écart-type maximum de 30).

---

### **Pièges à Éviter :**
- **Toujours viser 0 :** Risque de perdre si d'autres joueurs stabilisent la moyenne autour de 20–30.
- **Ignorer les nouvelles règles :** Une règle comme "les nombres pairs doublent leur poids" change radicalement la stratégie.

---

## **Règles Perturbatrices, Psychologiques et de Retour en Grâce**

Voici une liste de règles à ajouter à chaque **GAME OVER** pour pimenter le jeu et offrir des opportunités de retour aux joueurs en difficulté :

### **1. Règle du "Double Jeu"**  
**Effet :** Les joueurs avec **5 points négatifs ou plus** peuvent soumettre **deux nombres** au lieu d'un. Seul le plus proche du nombre gagnant est pris en compte.  
**Psychologie :** Donne un avantage aux "perdants" tout en créant de l'incertitude sur leur véritable stratégie.  
*Exemple :* Un joueur à -6 points choisit 25 et 35 → si le gagnant est 30, c’est 35 qui est retenu.

### **2. "Révolte des Perdants"**  
**Effet :** Tous les joueurs avec des points négatifs votent pour **soustraire un nombre (1-10)** de la moyenne finale.  
**Psychologie :** Les joueurs en difficulté sabotent les stratégies des leaders, forçant l’adaptation.  
*Exemple :* La moyenne est 40, mais les perdants votent pour soustraire 7 → nouvelle moyenne = 33.

### **3. "Joker Fantôme"**  
**Effet :** Le joueur éliminé (GAME OVER) choisit un **nombre secret** avant de partir. Ce nombre est ajouté aux propositions de la prochaine manche.  
**Psychologie :** Même éliminé, on influence le jeu → vengeance et chaos garantis.  
*Exemple :* Le fantôme choisit 0 → la moyenne baisse radicalement.

### **4. "Multiplicateur Inversé"**  
**Effet :** Si le nombre gagnant est **inférieur à 20**, le multiplicateur devient **1.2** au lieu de 0.8 pour la manche suivante.  
**Psychologie :** Brise les stratégies de nombres bas et force un revirement brutal.  
*Exemple :* Gagnant = 15 → prochaine manche : moyenne × 1.2.

### **5. "Pari Maudit"**  
**Effet :** Un joueur aléatoire (non-gagnant) voit son choix **divisé par 2** ou **multiplié par 1.5** (pile ou face).  
**Psychologie :** Introduit une peur du hasard, même pour les stratégies optimisées.  
*Exemple :* Un joueur choisit 40 → transformé en 20 (divisé par 2) ou 60 (×1.5).

### **6. "Immunité Éphémère"**  
**Effet :** Le joueur avec le **plus de points négatifs** devient immunisé : s’il perd, aucun point négatif n’est ajouté.  
**Psychologie :** Offre un répit aux perdants, forçant les autres à les cibler différemment.  
*Exemple :* Un joueur à -8 points rate le gagnant → reste à -8.

### **7. "Miroir Trompeur"**  
**Effet :** Le nombre gagnant est soit **moyenne × 0.8**, soit **100 – (moyenne × 0.8)** (choisi secrètement par l’hôte).  
**Psychologie :** Double le risque de se tromper → les joueurs doivent parier sur deux stratégies opposées.  
*Exemple :* Moyenne = 50 → gagnant = 40 **ou** 60.

### **8. "Alliance Interdite"**  
**Effet :** Les joueurs peuvent former des **équipes de 2** pour partager leurs points négatifs. Si l’un gagne, l’autre reçoit +3 points.  
**Psychologie :** Trahisons et loyautés émergent, surtout en fin de partie.  
*Exemple :* Deux alliés : l’un gagne → l’autre passe de -7 à -4.

### **9. "Règle du Chaos"**  
**Effet :** Le multiplicateur (0.8) change aléatoirement entre **0.5 et 1.0** pour une manche.  
**Psychologie :** Personne ne peut anticiper → les stratégies logiques deviennent risquées.  
*Exemple :* Multiplicateur = 1.0 → le gagnant = moyenne exacte (50 si tous choisissent 50).

### **10. "Vengeance Ultime"**  
**Effet :** Le dernier joueur éliminé peut **imposer un nombre** à un joueur restant pour la prochaine manche.  
**Psychologie :** Les éliminés restent dans la course psychologiquement, et les survivants sont piégés.  
*Exemple :* Le fantôme force un joueur à choisir 0 → baisse artificielle de la moyenne.

### **11. "Pari Transparent"**  
**Effet :** Tous les joueurs voient les choix des autres **en temps réel** avant de valider leur propre nombre (30 secondes pour ajuster).  
**Psychologie :** Course contre la montre, psychologie de groupe, et mimétisme stratégique.  
*Exemple :* Un joueur voit que beaucoup ont choisi 30 → il baisse à 24 pour viser 24 × 0.8 = 19.2.

### **12. "Règle du Sacrifice"**  
**Effet :** Un joueur peut volontairement prendre **+2 points négatifs** pour soustraire 10 à la moyenne.  
**Psychologie :** Stratégie altruiste ou égoïste pour sauver sa position ou faire tomber un rival.  
*Exemple :* Un joueur à -7 prend -2 points → la moyenne passe de 50 à 40.

### **13. "Règle de l’Écho"**  
**Effet :** Le nombre gagnant de la manche précédente est ajouté aux propositions de la manche actuelle (comme un "écho").  
**Psychologie :** Les joueurs doivent anticiper la persistance des stratégies passées, créant des cycles de surenchère.  
*Exemple :* Si le gagnant était 25, il est ajouté comme un choix fictif → influence la nouvelle moyenne.

### **14. "Boule de Cristal"**  
**Effet :** Un joueur aléatoire (non-gagnant) reçoit un indice sur la **fourchette du nombre gagnant** (ex: "entre 20 et 40") avant de choisir.  
**Psychologie :** Crée des inégalités stratégiques et de la méfiance envers le "favorisé".  
*Exemple :* Le joueur averti choisit 30, tandis que les autres spéculent sur l’indice.

### **15. "Règle du Pacte"**  
**Effet :** Deux joueurs peuvent **échanger leurs points négatifs** avant une manche. Si l’un des deux gagne, les points échangés sont annulés.  
**Psychologie :** Encourage les alliances risquées et les coups de théâtre.  
*Exemple :* Un joueur à -8 échange avec un joueur à -2 → si l’un gagne, les deux reviennent à 0.

### **16. "Temps Révolu"**  
**Effet :** Le multiplicateur (0.8) est remplacé par la **moyenne des multiplicateurs des 3 dernières manches**.  
**Psychologie :** Rend les stratégies à long terme imprévisibles et force l’analyse historique.  
*Exemple :* Multiplicateurs précédents = 0.8, 1.2, 0.5 → nouveau multiplicateur = 0.83.

### **17. "Règle du Mimétisme"**  
**Effet :** Si plus de 50% des joueurs choisissent le même nombre, ce nombre est automatiquement **divisé par 2**.  
**Psychologie :** Décourage le suivi de groupe et récompense l’originalité.  
*Exemple :* 6 joueurs sur 10 choisissent 40 → tous sont ajustés à 20.

### **18. "Paradoxe Temporel"**  
**Effet :** Le joueur qui gagne une manche voit son choix **remplacer le nombre gagnant de la manche précédente** dans l’historique.  
**Psychologie :** Réécrit le passé, perturbant les stratégies basées sur les tendances.  
*Exemple :* Si le gagnant actuel est 30, et que la manche précédente était 25 → l’historique affiche maintenant 30.

### **19. "Règle du Bilan"**  
**Effet :** À chaque manche, les joueurs avec des points négatifs peuvent **ajouter leur score négatif à leur nombre choisi** (ex: -5 → nombre +5).  
**Psychologie :** Les "perdants" montent mécaniquement dans la fourchette haute, brouillant les anticipations.  
*Exemple :* Un joueur à -7 choisit 20 → son nombre devient 27.

### **20. "Joker Aléatoire"**  
**Effet :** Un nombre entre 0 et 100 est généré aléatoirement et ajouté aux propositions.  
**Psychologie :** Introduit un élément de chaos pur, avantageant les joueurs qui osent parier sur l’aléatoire.  
*Exemple :* Le joker est 73 → la moyenne augmente si personne ne l’avait anticipé.

### **21. "Règle de l’Équilibriste"**  
**Effet :** Si un joueur choisit exactement le nombre gagnant, il peut **retirer 2 points négatifs** ou en **donner 2 à un adversaire**.  
**Psychologie :** Récompense les coups précis et encourage la rivalité ciblée.  
*Exemple :* Un joueur à -4 gagne exactement → il passe à -2 ou met un rival à -9.

### **22. "Vortex des Extrêmes"**  
**Effet :** Les nombres les plus bas (0-10) et les plus hauts (90-100) sont **exclus de la moyenne**, mais leurs auteurs reçoivent +1 point négatif.  
**Psychologie :** Décourage les stratégies extrêmes tout en piégeant les joueurs téméraires.  
*Exemple :* Un joueur choisit 3 → son nombre est ignoré, et il reçoit -1.

### **23. "Règle du Momentum"**  
**Effet :** Si un joueur gagne deux manches consécutives, il **fixe le multiplicateur** (entre 0.5 et 1.5) pour la prochaine manche.  
**Psychologie :** Crée un "boss" à abattre, unissant les autres joueurs contre lui.  
*Exemple :* Un joueur dominant fixe le multiplicateur à 1.5 → la moyenne explose.

### **24. "Règle du Doute"**  
**Effet :** Les joueurs peuvent **mentir sur leur nombre choisi** une fois par partie. Le mensonge est révélé après la manche.  
**Psychologie :** Instaure une paranoïa généralisée et des stratégies de bluff.  
*Exemple :* Un joueur annonce 40 mais a vraiment choisi 28 → perturbation des calculs des autres.

### **25. "Règle du Phénix"**  
**Effet :** Lorsqu’un joueur atteint **GAME OVER**, il relance avec **0 point négatif**, mais ne peut plus gagner pendant 3 manches.  
**Psychologie :** Les "morts-vivants" perturbent le jeu sans pression immédiate, créant un effet de surprise.  
*Exemple :* Un joueur éliminé revient et choisit 100 pour saboter la moyenne.

---

### **Conseil pour l’Hôte :**  
Mélangez ces règles avec celles précédentes pour maintenir un équilibre entre **chaos calculé** et **espoir pour les perdants**. Annoncez les nouvelles règles de manière théâtrale pour amplifier leur impact psychologique (ex: *"Cette nuit, les fantômes reviennent hanter vos choix..."*). Plus les joueurs doivent jongler entre logique, intuition et trahisons, plus le jeu devient mémorable ! 🎮✨

---

**En Résumé :** Combinez logique itérative (\(0,8 \times\) moyenne anticipée) et observation des comportements adverses. Adaptez-vous aux règles émergentes pour survivre aux manches ultérieures. 

Amusez-vous bien et que la chance soit avec vous dans Balance Scale! 🎲✨