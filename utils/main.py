# XML data from https://github.com/cmeeren/zelda-optimal-equipment-guides
import xml.etree.ElementTree as ET
import json
from zelda_data import parse_zelda_data

# Set the XML file path
xml_file_path = 'xml_source/wind-waker-hd.xml'

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Call the parsing function
game_data = parse_zelda_data(root)

# Convert game_data dictionary to JSON format
json_data = json.dumps(game_data, indent=4)

# JSON output path
json_file_path = 'output/game_segments.json'

# Write JSON data to file
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Game data successfully written to {json_file_path}")

print(json_data)
