import os
from PIL import Image

folder_path = 'assets\seeds'
dest_path = 'assets\seeds'
images = os.listdir(folder_path)


image_path = os.path.join(folder_path, 'Everbloom_seed_asset.png')
img = Image.open(image_path)
width, height = img.size

img = img.crop((0, 0, 587, 707))

img = img.resize((30, 30))
destination = os.path.join(dest_path, 'Everbloom_seed.png')
img.save(destination)

# make an array of images that are cropped from 0, 0 to 1072, 1541
# and then resized to 50x100

