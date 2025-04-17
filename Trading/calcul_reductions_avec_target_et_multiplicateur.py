# Entrée du prix initial
prix_initial = float(input("Entrez le prix initial ($): "))

# Entrée de la liste des pourcentages de chute
liste_input = input(
    "Entrez la liste des pourcentages de chute (séparés par des virgules, ex. 50, 10, 10, 5) : "
)
pourcentages = [float(x.strip()) / 100 for x in liste_input.split(",")]

# Entrée du prix cible
prix_cible = float(input("Entrez le prix cible ($): "))

# Vérification des entrées
if prix_initial <= 0 or prix_cible <= 0:
    print("Erreur : Le prix initial et le prix cible doivent être positifs.")
    exit()
if not pourcentages or any(p < 0 for p in pourcentages):
    print("Erreur : Les pourcentages doivent être des nombres positifs ou nuls.")
    exit()


# Fonction pour calculer le prix après une réduction
def appliquer_reduction(prix, taux):
    return prix * (1 - taux)


# Fonction pour calculer le pourcentage de hausse nécessaire
def calculer_hausse(prix_actuel, prix_cible):
    if prix_actuel == 0:  # Éviter la division par zéro
        return float("inf") if prix_cible > 0 else 0
    hausse = (prix_cible - prix_actuel) / prix_actuel * 100
    return hausse


# Fonction pour calculer le multiplicateur nécessaire
def calculer_multiplicateur(prix_actuel, prix_cible):
    if prix_actuel == 0:  # Éviter la division par zéro
        return float("inf") if prix_cible > 0 else 0
    multiplicateur = prix_cible / prix_actuel
    return multiplicateur


# Calcul et affichage des résultats étape par étape
prix_actuel = prix_initial
print(f"\nPrix initial : {prix_actuel:.2f} $")
print(
    f"Hausse nécessaire pour {prix_cible:.2f} $ : {calculer_hausse(prix_actuel, prix_cible):.2f}%"
)
print(
    f"Multiplicateur pour {prix_cible:.2f} $ : ×{calculer_multiplicateur(prix_actuel, prix_cible):.2f}"
)

for i, taux in enumerate(pourcentages, 1):
    prix_actuel = appliquer_reduction(prix_actuel, taux)
    hausse = calculer_hausse(prix_actuel, prix_cible)
    multiplicateur = calculer_multiplicateur(prix_actuel, prix_cible)
    print(
        f"\nÉtape {i} : Réduction de {taux * 100:.0f}% -> Prix obtenu : {prix_actuel:.2f} $"
    )
    print(f"Hausse nécessaire pour {prix_cible:.2f} $ : {hausse:.2f}%")
    print(f"Multiplicateur pour {prix_cible:.2f} $ : ×{multiplicateur:.2f}")

# Affichage du prix final
print(f"\nPrix final après toutes les réductions : {prix_actuel:.2f} $")
print(
    f"Hausse nécessaire pour atteindre {prix_cible:.2f} $ : {calculer_hausse(prix_actuel, prix_cible):.2f}%"
)
print(
    f"Multiplicateur pour atteindre {prix_cible:.2f} $ : ×{calculer_multiplicateur(prix_actuel, prix_cible):.2f}"
)
