from itertools import product
from Utils.path_utils import get_single_folder_path

# Entrées utilisateur
prix_initial = float(input("Entrez le prix initial ($): "))
prix_final = float(input("Entrez le prix final ($): "))
max_iterations = int(input("Entrez le nombre maximal d'itérations : "))

# Vérification des entrées
if (
    prix_initial <= 0
    or prix_final <= 0
    or prix_final >= prix_initial
    or max_iterations <= 0
):
    print(
        "Erreur : Les prix doivent être positifs, le prix final doit être inférieur au prix initial, et le nombre d'itérations maximal doit être positif."
    )
    exit()

# Liste des pourcentages de réduction possibles (1% à 10%)
taux_reductions = [i / 100 for i in range(1, 11)]  # [0.01, 0.02, ..., 0.10]


# Fonction pour calculer le prix après une série de réductions
def calculer_prix_final(prix_init, reductions):
    prix = prix_init
    for taux in reductions:
        prix *= 1 - taux
    return prix


# Fonction pour convertir les taux en pourcentages lisibles
def format_reductions(reductions):
    return [f"{int(taux * 100)}%" for taux in reductions]


# Stockage des combinaisons valides
combinaisons_valides = []

# Générer toutes les combinaisons possibles jusqu'à max_iterations
for longueur in range(1, max_iterations + 1):
    for combinaison in product(taux_reductions, repeat=longueur):
        prix_obtenu = calculer_prix_final(prix_initial, combinaison)
        if prix_obtenu <= prix_final:  # Le prix final est atteint ou dépassé
            somme_pourcentages = sum([taux * 100 for taux in combinaison])
            combinaisons_valides.append((combinaison, prix_obtenu, somme_pourcentages))

# Trier les combinaisons selon les critères
# 1. Somme des pourcentages (croissant)
# 2. Nombre d'itérations (croissant)
# 3. Dernier élément (croissant)
combinaisons_valides.sort(key=lambda x: (x[2], len(x[0]), x[0][-1]))

# Écriture des combinaisons dans le premier fichier
file_name_combination = "combinaisons_reductions.txt"
nom_fichier_combinaisons = get_single_folder_path(file_name_combination)

with open(nom_fichier_combinaisons, "w", encoding="utf-8") as fichier:
    if not combinaisons_valides:
        fichier.write(
            f"Aucune combinaison ne permet d'atteindre ou dépasser {prix_final:.2f} $ en {max_iterations} itérations ou moins.\n"
        )
    else:
        fichier.write(
            f"Combinaisons possibles pour atteindre ou dépasser {prix_final:.2f} $ en {max_iterations} itérations maximum :\n\n"
        )
        for i, (combinaison, prix, somme) in enumerate(combinaisons_valides, 1):
            reductions_pct = format_reductions(combinaison)
            fichier.write(
                f"Combinaison {i} : {reductions_pct} -> Prix obtenu : {prix:.2f} $ (Somme : {somme:.0f}%, {len(combinaison)} itérations)\n"
            )

# Préparation des résultats à afficher et à écrire dans le second fichier
file_name_reslt_opti = "resultats_optimaux.txt"
nom_fichier_resultats = get_single_folder_path(file_name_reslt_opti)

resultats = []
if not combinaisons_valides:
    resultats.append(
        f"Aucune combinaison ne permet d'atteindre ou dépasser {prix_final:.2f} $ en {max_iterations} itérations ou moins."
    )
    resultats.append(
        f"Voir le fichier '{nom_fichier_combinaisons}' pour plus de détails."
    )
else:
    resultats.append(
        f"Nombre total de combinaisons trouvées : {len(combinaisons_valides)}"
    )
    resultats.append(
        f"Les combinaisons ont été écrites dans le fichier '{nom_fichier_combinaisons}'."
    )

    # Meilleure combinaison (première après tri)
    meilleure_combinaison, meilleur_prix, meilleure_somme = combinaisons_valides[0]
    reductions_pct_optimal = format_reductions(meilleure_combinaison)
    resultats.append(f"Combinaison optimale : {reductions_pct_optimal}")
    resultats.append(f"Prix obtenu : {meilleur_prix:.2f} $")
    resultats.append(f"Somme des pourcentages : {meilleure_somme:.0f}%")
    resultats.append(f"Nombre d'itérations : {len(meilleure_combinaison)}")

# Affichage à l’écran
print("\n" + "\n".join(resultats))

# Écriture des résultats dans le second fichier
with open(nom_fichier_resultats, "w", encoding="utf-8") as fichier:
    fichier.write("\n".join(resultats) + "\n")

print(
    f"\nLes résultats affichés ont été écrits dans le fichier '{nom_fichier_resultats}'."
)
