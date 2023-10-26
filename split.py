import os
import json
import datetime  # Pour obtenir la date et l'heure actuelles

# Function to split a file into parts and store them in Primary.fesf and Secondary.fesf files
def split_and_store_file(input_file_name, part_size):
    try:
        with open(input_file_name, 'rb') as input_file, \
             open('Primary.fesf', 'wb') as primary_file, \
             open('Secondary.fesf', 'wb') as secondary_file:

            while True:
                part = input_file.read(part_size)
                if not part:
                    break

                # Alternate between Primary and Secondary files
                primary_file.write(part)
                part = input_file.read(part_size)
                if not part:
                    break
                secondary_file.write(part)

        print("File split and stored successfully.")

        # Create the configuration file with part size
        config = {
            "part_size": part_size,
        }
        with open('config.json', 'w') as config_file:
            config_file.write(json.dumps(config, indent=4))
            print("Configuration file 'config.json' created successfully.")

        # Remove the input file (temp.tef)
        os.remove(input_file_name)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    input_file_name = "temp.tef"
    part_size = int(input("Enter the size of each part in bytes: "))

    split_and_store_file(input_file_name, part_size)

