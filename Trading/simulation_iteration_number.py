import math

# Entrées utilisateur
prix_initial = float(input("Entrez le prix initial ($): "))
prix_final = float(input("Entrez le prix final ($): "))
taux_reduction = (
    float(input("Entrez le pourcentage de réduction par itération (%): ")) / 100
)

# Vérification que les entrées sont cohérentes
if (
    prix_initial <= 0
    or prix_final <= 0
    or taux_reduction <= 0
    or prix_final >= prix_initial
):
    print(
        "Erreur : Les prix doivent être positifs, le prix final doit être inférieur au prix initial, et le taux de réduction doit être positif."
    )
else:
    # Calcul du nombre d'itérations
    # Formule : prix_final = prix_initial * (1 - taux_reduction)^n
    # Donc : n = log(prix_final / prix_initial) / log(1 - taux_reduction)
    nombre_iterations = math.log(prix_final / prix_initial) / math.log(
        1 - taux_reduction
    )

    # Arrondi au nombre entier supérieur et inférieur pour donner une plage
    iterations_inf = int(nombre_iterations)  # Partie entière inférieure
    iterations_sup = math.ceil(nombre_iterations)  # Partie entière supérieure

    # Vérification des prix avec ces itérations
    prix_apres_inf = prix_initial * (1 - taux_reduction) ** iterations_inf
    prix_apres_sup = prix_initial * (1 - taux_reduction) ** iterations_sup

    # Affichage des résultats
    print(f"\nNombre d'itérations théorique : {nombre_iterations:.4f}")
    print(f"Avec {iterations_inf} itérations, le prix serait : {prix_apres_inf:.2f} $")
    print(f"Avec {iterations_sup} itérations, le prix serait : {prix_apres_sup:.2f} $")
    print(
        f"\nConclusion : Il faut entre {iterations_inf} et {iterations_sup} itérations pour atteindre ou dépasser le prix final de {prix_final:.2f} $."
    )
