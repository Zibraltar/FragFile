import json
from cryptography.fernet import Fernet
import os

def decrypt_file(input_file, key):
    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    return decrypted_data

def main():
    try:
        with open("key.json", "r") as key_file:
            key_dict = json.load(key_file)
            key = key_dict["key"].encode()

        decrypted_data = decrypt_file("temp.tef", key)

        with open("info.json", "r") as info_file:
            info_dict = json.load(info_file)
            file_name = info_dict["file_name"]

        with open(file_name, "wb") as output_file:
            output_file.write(decrypted_data)

        print(f"Fichier déchiffré avec succès : {file_name}")

	# Supprimez les fichiers
        os.remove("config.json")
        os.remove("info.json")
        os.remove("key.json")
        os.remove("temp.tef")
    except Exception as e:
        print(f"Erreur : {str(e)}")


if __name__ == "__main__":
    main()
