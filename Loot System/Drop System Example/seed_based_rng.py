import random


def seed_based_rng(seed):
    random.seed(seed)
    return random.randint(1, 100)


# Simulation
print(f"Résultat reproductible avec la graine 42 : {seed_based_rng(42)}")
