import yaml
import json

# Load docker-compose.yaml
with open('docker-compose.yaml', 'r') as file:
    yaml_content = yaml.safe_load(file)

# Print parsed YAML as Python dict
print("Parsed YAML:")
print(json.dumps(yaml_content, indent=4))

# Convert YAML to JSON and save it
with open('docker-compose.json', 'w') as json_file:
    json.dump(yaml_content, json_file, indent=4)

print("\nYAML successfully converted to JSON → docker-compose.json")