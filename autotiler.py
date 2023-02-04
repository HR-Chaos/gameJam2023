import os
from PIL import Image
import pygame
import numpy as np

def make_tile_array(tile_size):
    main_img = Image.open('assets\MossyTileset\Mossy-TileSet.png')
    # cropped_image = img.crop((0, 0, 512, 512))
    sprites = []
    width, height = main_img.size
    # create an empty image
    img = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
    img = img.resize((tile_size, tile_size))
    sprites.append(img)

    print(width/512, height)
    for row in range(0, width, 512):
        for col in range(0, height, 512):
            cropped_image = main_img.crop((row, col, row + 512, col + 512))
            img = cropped_image.resize((tile_size, tile_size))
            sprites.append(img)
    return sprites

def make_map():
    map = [[0] * 10 for i in range(10)]
    for i in range(8):
        for j in range(10):
            map[i][j] = 0
            if i == 5:
                map[i][j] = 8
            if i == 6:
                map[i][j] = 10
    return map