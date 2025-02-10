def conditional_drop(time_taken):
    if time_taken < 120:  # Moins de 2 minutes
        return "Épée légendaire obtenue!"
    else:
        return "Temps trop long, pas d'épée légendaire."


# Simulation
print(conditional_drop(90))  # Temps pris : 90 secondes
