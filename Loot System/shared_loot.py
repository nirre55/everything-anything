import random


def shared_loot(players):
    winner = random.choice(players)
    return f"{winner} a gagné le loot!"


# Simulation
print(shared_loot(["Joueur1", "Joueur2", "Joueur3"]))
