import os
import json

# Function to combine Primary.fesf and Secondary.fesf files into a single file
def combine_files():
    try:
        with open('Primary.fesf', 'rb') as primary_file, \
             open('Secondary.fesf', 'rb') as secondary_file, \
             open('config.json', 'r') as config_file:

            config = json.load(config_file)
            part_size = config["part_size"]

            with open('temp.tef', 'wb') as combined_file:
                while True:
                    part_primary = primary_file.read(part_size)
                    if not part_primary:
                        break
                    combined_file.write(part_primary)
                    part_secondary = secondary_file.read(part_size)
                    if not part_secondary:
                        break
                    combined_file.write(part_secondary)

        print("Primary.fesf and Secondary.fesf files combined successfully into 'temp.tef'.")

        # Remove Primary.fesf and Secondary.fesf files
        os.remove('Primary.fesf')
        os.remove('Secondary.fesf')
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    combine_files()
