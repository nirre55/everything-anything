# Prix initial
prix_initial = 1000
prix = prix_initial
taux_reduction = 0.01  # 1% de réduction
iterations = 10

# Affichage du prix initial
print(f"Prix initial : {prix_initial:.2f} $")

# Boucle pour les 10 itérations
for i in range(iterations):
    prix = prix * (1 - taux_reduction)  # Réduction de 1%
    print(f"Itération {i + 1} : {prix:.2f} $")

# Calcul du pourcentage de chute
pourcentage_chute = ((prix_initial - prix) / prix_initial) * 100

# Affichage du résultat final et du pourcentage de chute
print(f"\nPrix final après {iterations} itérations : {prix:.2f} $")
print(f"Pourcentage de chute par rapport au prix initial : {pourcentage_chute:.2f} %")

# Vérification avec la formule directe
prix_final_formule = prix_initial * (1 - taux_reduction) ** iterations
print(f"Vérification avec formule directe : {prix_final_formule:.2f} $")
