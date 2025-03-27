# Trading
Un folder qui regroupe quelques idee sur le trading

## Le fichier `simulation.py` :

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
    - Une formule directe (prix_initial * (1 - taux_reduction) ** iterations) est utilisée pour confirmer le résultat.