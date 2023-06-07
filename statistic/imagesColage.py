import os
from PIL import Image
import re

def extract_number(string):
    number = re.search(r'\d+', string)
    if number:
        return int(number.group())
    else:
        return None
    
folder_path = "../graphs/conf/python"

output_folder = "../graphs/conf/pythonGrouped"

image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

image_groups = {}
for image_file in image_files:
    image_number = extract_number(image_file)
    if image_number not in image_groups:
        image_groups[image_number] = []
    image_groups[image_number].append(image_file)

print(image_groups)

for image_number, image_group in image_groups.items():
    images_to_combine = []
    for image_file in image_group:
        image_path = os.path.join(folder_path, image_file)
        image = Image.open(image_path)
        images_to_combine.append(image)

    width = sum(image.width for image in images_to_combine)
    height = max(image.height for image in images_to_combine)

    combined_image = Image.new('RGB', (width, height))

    x_offset = 0
    for image in images_to_combine:
        combined_image.paste(image, (x_offset, 0))
        x_offset += image.width

    combined_image_path = os.path.join(output_folder, str(image_number) + ".jpg")
    combined_image.save(combined_image_path)

    print(f"Combined image saved: {combined_image_path}")
