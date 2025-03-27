# Trading
Un folder qui regroupe quelques idee sur le trading

## Le fichier `simulation_final_price.py` :

un script Python qui simule la réduction de X % sur Y itérations à partir d'un prix initial de Z $, affiche chaque étape, puis calcule le pourcentage de chute par rapport au prix de départ

### Explication : 

1. **Variables initiales :**
    - prix_initial : Le prix de départ (1000 $).
    - prix : Variable qui sera mise à jour à chaque itération.
    - taux_reduction : 1 % (0.01).
    - iterations : Nombre d’itérations (10).

2. **Boucle :**
    - À chaque tour, le prix est multiplié par 1−0.01=0.99, simulant une réduction de 1 %.
    - Le résultat est affiché avec 2 décimales pour plus de lisibilité.

3. **Calcul du pourcentage de chute :**
    - On calcule la différence entre le prix initial et le prix final, divisée par le prix initial, puis multipliée par 100.

4. **Vérification :**
    - Une formule directe `(prix_initial * (1 - taux_reduction) ** iterations)` est utilisée pour confirmer le résultat.


## Le fichier `simulation_iteration_number.py` :

Un script Python qui prend un prix initial, un prix final et un pourcentage de chute par itération, puis calcule le nombre d'itérations nécessaires pour passer du prix initial au prix final avec cette réduction répétée

### Explication : 

1. **Entrées :**
    - L’utilisateur entre le prix initial, le prix final et le pourcentage de réduction par itération (ex. 1 pour 1 %).

2. **Vérification :**
    - Le script vérifie que les valeurs sont cohérentes : prix positifs, prix final inférieur au prix initial, et taux de réduction positif.

3. **Calcul du nombre d’itérations :**
    - On utilise la formule mathématique dérivée de `{prix_final} = {prix_initial} \times (1 - {taux_reduction})^n`.
    - En isolant ( n ), on obtient : `n = \frac{\log({prix_final} / {prix_initial})}{\log(1 - {taux_reduction})}`.
    - Le module math est utilisé pour les calculs logarithmiques.

4. **Résultat :**
    - Comme le nombre d’itérations est souvent un nombre décimal, le script donne la valeur théorique exacte, puis calcule les prix obtenus avec l’entier inférieur et supérieur pour montrer où se situe le prix final.