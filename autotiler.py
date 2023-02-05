import os
from PIL import Image
import pygame
import numpy as np

main_img = Image.open('assets\MossyTileset\Mossy-TileSet.png')

def make_tile_array(tile_size):
    # cropped_image = img.crop((0, 0, 512, 512))
    sprites = []
    width, height = main_img.size
    # create an empty image
    img = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
    img = img.resize((tile_size, tile_size))
    sprites.append(img)

    for row in range(0, width, 512):
        for col in range(0, height, 512):
            cropped_image = main_img.crop((row, col, row + 512, col + 512))
            img = cropped_image.resize((tile_size, tile_size))
            sprites.append(img)
    return sprites

def make_map(screen, tile_size):
    width, height = screen.get_size()
    width = width//tile_size
    height = height//tile_size
    map = [[0] * width for i in range(height)]
    for i in range(height):
        for j in range(width):
            map[i][j] = 0
            if i == 11:
                map[i][j] = 8
            if i == 12:
                map[i][j] = 10
    return map