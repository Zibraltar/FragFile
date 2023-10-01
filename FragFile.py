import os
import json

# Function to split a file into parts and store them in PCF and SCF files
def split_and_store_file(input_file_name, part_size):
    try:
        with open(input_file_name, 'rb') as input_file, \
             open('PCF', 'wb') as pcf_file, \
             open('SCF', 'wb') as scf_file:

            while True:
                part = input_file.read(part_size)
                if not part:
                    break

                # Alternate between PCF and SCF files
                pcf_file.write(part)
                part = input_file.read(part_size)
                if not part:
                    break
                scf_file.write(part)

        print("File split and stored successfully.")

        # Create the configuration file
        config = {
            "input_file_name": input_file_name,
            "extension": os.path.splitext(input_file_name)[1],
            "part_size": part_size
        }
        with open('config.json', 'w') as config_file:
            config_file.write(json.dumps(config, indent=4))
            print("Configuration file 'config.json' created successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Function to combine PCF and SCF files into a single file
def combine_files():
    try:
        with open('PCF', 'rb') as pcf_file, \
             open('SCF', 'rb') as scf_file, \
             open('config.json', 'r') as config_file:

            config = json.load(config_file)
            input_file_name = config["input_file_name"]
            extension = config["extension"]
            part_size = config["part_size"]

            with open(f'{input_file_name}{extension}', 'wb') as combined_file:
                while True:
                    part_pcf = pcf_file.read(part_size)
                    part_scf = scf_file.read(part_size)
                    if not part_pcf and not part_scf:
                        break
                    if part_pcf:
                        combined_file.write(part_pcf)
                    if part_scf:
                        combined_file.write(part_scf)

        print(f"PCF and SCF files combined successfully into '{input_file_name}{extension}'.")
        print(f"Restored with a part size of {part_size} bytes.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    choice = input("Do you want to split a file (S) or combine into a single file (C)? : ").upper()

    if choice == 'S':
        input_file_name = input("Enter the name of the file to split: ")
        part_size = int(input("Enter the size of each part in bytes: "))

        split_and_store_file(input_file_name, part_size)
    elif choice == 'C':
        combine_files()
    else:
        print("Invalid choice. Please enter 'S' to split or 'C' to combine.")

