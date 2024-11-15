import os
import json
from yaml_reader.reader import read_yaml_from_folder


def process_and_save_files(input_folder, output_folder):
    yaml_data = read_yaml_from_folder(input_folder)

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each YAML file data and write it to a JSON file in the output directory
    for i, data in enumerate(yaml_data, start=1):
        output_file_path = os.path.join(output_folder, f"output_{i}.json")
        with open(output_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Processed file saved to {output_file_path}")


def main():
    input_folder = "./input"
    output_folder = "./output"
    process_and_save_files(input_folder, output_folder)


if __name__ == "__main__":
    main()
