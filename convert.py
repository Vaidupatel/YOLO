from pathlib import Path
import json

# Folder containing JSON files
json_folder = Path(r'D:\Project\Carpetweeds\Label')

# Loop through JSON files
for json_file in json_folder.glob('*.json'):

  # Load JSON data
  with open(json_file) as f:
    data = json.load(f)

  label = data['shapes'][0]['label']
  points = data['shapes'][0]['points']

  if label == "weeds":
    label = "1"
  else:
    label = "0"

  point_str = ' '.join([str(p) for coords in points for p in coords])

  # Construct output text file path
  txt_file = json_file.with_suffix('.txt')

  # Write label and points to text file
  with open(txt_file, 'w') as f:
    f.write(label + ' ' + point_str)