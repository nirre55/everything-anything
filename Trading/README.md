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


## Le fichier `simulation_combination generation.py` :

un script Python qui génère des combinaisons de pourcentages de chute (de 1 % à 10 %) pour passer d’un prix initial à un prix final, en respectant un nombre maximal d’itérations défini par l’utilisateur. Le script cherchera toutes les combinaisons possibles et identifiera la combinaison optimale (celle qui utilise le moins d’itérations tout en atteignant ou dépassant le prix final sans dépasser le maximum d’itérations).

### Explications :

1. **Entrées et validation :**  
    - Le prix initial  
    - Le prix final  
    - Le nombre maximum d'itérations (`max_iterations`)  
    avec les vérifications nécessaires.

2. **Pourcentages appliqués  :**  
Les taux de réduction/promotion utilisés vont de :  
`1% à 10%` (soit `0.01 à 0.10` en valeur décimale).

3. **Génération des combinaisons :**  
Méthode :  
    - Utilisation de `product` pour générer toutes les combinaisons possibles (de 1 à `max_iterations`)  
    - Pour chaque combinaison générée, nous calculons :  
    - Le prix obtenu après application des promotions  
    - La somme cumulée des pourcentages appliqués  

4. **Tri et sélection des combinaisons :**  
Critères de tri (appliqués via `sort`) :  
    - Somme des pourcentages (priorité principale)  
    - Nombre d'itérations (priorité secondaire)  
    - Dernier élément de la combinaison (critère tertiaire)  

5. **Résultats en sortie :**  
    - **Affichage** :  
        - **Toutes les combinaisons valides** (où `prix obtenu ≤ prix final`) avec :  
            - Prix final calculé  
            - Somme des % appliqués  
            - Nombre d'itérations  
        - **Combinaison optimale** : Premier résultat du tri (meilleur compromis).  
    - **Fichiers** :
        - `combinaisons_reductions.txt` : Contient toutes les combinaisons valides, comme dans la version précédente.
        - `resultats_optimaux.txt` : Contient exactement ce qui est affiché à l’écran (nombre total de combinaisons et détails de la combinaison optimale).


## Le fichier `calcul_reductions_avec_target_et_multiplicateur.py` :

Ce script prend un prix initial, une liste de pourcentages de chute, et un prix cible (target). Pour chaque réduction, il calcule le prix obtenu, puis le pourcentage de hausse nécessaire pour atteindre le prix cible à partir du prix actuel et le multiplicateur nécessaire pour passer du prix actuel au prix cible après chaque réduction.

### Explications :

1. **Entrées :**  
    - Le prix initial  
    - Le prix target
    - Liste de pourcentage de chute 

2. **Vérifications  :**  
    - Vérifie que le prix initial et le prix cible sont positifs.
    - Vérifie que les pourcentages sont valides (non négatifs).

3. **Fonctions :** 
    - `appliquer_reduction` : Calcule le prix après une réduction.

    - `calculer_hausse` : Calcule le pourcentage de hausse nécessaire pour passer du prix actuel au prix cible avec la formule : \text{Hausse} = \frac{\text{prix_cible} - \text{prix_actuel}}{\text{prix_actuel}} \times 100.

    - `calculer_multiplicateur` : Calcule le facteur par lequel il faut multiplier le prix actuel pour atteindre le prix cible : \text{Multiplicateur} = \frac{\text{prix_cible}}{\text{prix_actuel}}.

4. **Sortie  :**  
Pour chaque étape (y compris le prix initial), le script affiche :  
    - Le prix actuel.
    - Le pourcentage de hausse nécessaire.
    - Le multiplicateur (avec le symbole × pour plus de clarté).


## Le fichier `binance_trading_testnet.py`

Un script Python pour le trading automatisé de contrats à terme sur l'échange Binance en utilisant la bibliothèque CCXT. Ce script permet d'ouvrir des positions au marché et à cours limité avec des ordres de take-profit (TP) et stop-loss (SL), de gérer l'effet de levier et la balance. Il est conçu pour fonctionner à la fois en environnement de test (testnet) et en production.

### Fonctionnalités
- Connexion au marché des futures de Binance via CCXT.
- Support des ordres au marché et à cours limité avec TP/SL.
- Configuration de l'effet de levier et calcul de la taille des positions basé sur un pourcentage de la balance.
- Mode testnet pour des tests sécurisés.
- Gestion des erreurs pour des opérations de trading robustes.
- Chargement des variables d'environnement pour une gestion sécurisée des clés API.

### Configuration
- Mode Testnet : Définissez use_testnet=True pour tester sur l'environnement testnet de Binance sinon Prod.
- Effet de levier : Ajustez l'effet de levier avec set_leverage(symbol, leverage). Par défaut, 10x.
- Taille des positions : Spécifiez le pourcentage de la balance à utiliser pour chaque trade (par exemple, percentage=10 pour 10 %).

### Remarques
- La fonction `open_limite_position_with_tp_and_sl` est actuellement supportée uniquement sur OKX en raison des limitations des exchanges.
- Les ordres TP/SL pour les positions à cours limité ne sont pas supportés sur Binance ; utilisez `open_market_position_then_add_tp_sl` à la place.
- Une seule position avec TP/SL peut être ouverte à la fois par symbole.
- Assurez-vous d'avoir une balance suffisante sur votre compte Binance (testnet ou production).

