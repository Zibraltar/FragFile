import tkinter as tk
from tkinter import filedialog
from cryptography.fernet import Fernet
import json
import os

def generate_key():
    key = Fernet.generate_key()
    key_dict = {"key": key.decode()}  # Convertir la clé en une chaîne de caractères pour JSON
    with open("key.json", "w") as key_file:
        json.dump(key_dict, key_file)

def encrypt_file(input_file, key):
    with open(input_file, "rb") as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open("temp.tef", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def select_file():
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale de Tkinter

    file_path = filedialog.askopenfilename()
    if file_path:
        generate_key()  # Générer une clé de cryptage
        with open("key.json", "r") as key_file:
            key_dict = json.load(key_file)
            key = key_dict["key"].encode()  # Convertir la clé en bytes pour Fernet

        encrypt_file(file_path, key)  # Crypter le fichier sélectionné

        # Créer un fichier info.json avec le nom du fichier (uniquement le nom, pas le chemin)
        file_name = os.path.basename(file_path)
        info_dict = {"file_name": file_name}
        with open("info.json", "w") as info_file:
            json.dump(info_dict, info_file)

        print(f"Le fichier {file_name} a été crypté avec succès en temp.tef.")
        print(f"Le nom du fichier a été enregistré dans info.json.")

if __name__ == "__main__":
    select_file()
