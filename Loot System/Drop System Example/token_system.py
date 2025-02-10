def token_system(tokens):
    if tokens >= 100:
        return "Objet rare acheté avec 100 jetons!"
    else:
        return f"Encore {100 - tokens} jetons nécessaires."


# Simulation
print(token_system(85))  # Jetons actuels : 85
