import os
from PIL import Image

folder_path = 'assets\player'
dest_path = 'assets\mushroom'
images = os.listdir(folder_path)

for image in images:
    image_path = os.path.join(folder_path, image)
    img = Image.open(image_path)
    width, height = img.size

    img = img.crop((0, 0, 1072, 1555))

    img = img.resize((75, 100))
    destination = os.path.join(dest_path, image)
    img.save(destination)

# make an array of images that are cropped from 0, 0 to 1072, 1541
# and then resized to 50x100

