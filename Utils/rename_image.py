import os


def rename_image_in_folder(folder_path, current_name, new_name):
    """
    Renomme une image dans un dossier en gardant la même extension.

    Args:
        folder_path (str): Chemin du dossier contenant l'image.
        current_name (str): Nom actuel de l'image (avec extension).
        new_name (str): Nouveau nom de l'image (sans extension).
    """
    old_path = os.path.join(folder_path, current_name)

    if not os.path.isfile(old_path):
        print(f"Le fichier '{current_name}' n'existe pas dans '{folder_path}'.")
        return

    _, ext = os.path.splitext(current_name)  # Récupérer l'extension
    new_path = os.path.join(folder_path, new_name + ext)  # Conserver l'extension

    os.rename(old_path, new_path)
    print(f"Image renommée : {current_name} -> {new_name + ext}")
