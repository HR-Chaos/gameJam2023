import pygame
from PIL import Image
#-------------------------- Level 1
def get_level_1():
    level = [[0]*24 for i in range(16)]
    counter = 0
    for i in range(0, 16, 1):
        for j in range(0, 24, 1): 
            if counter >= 0:
                pass
            elif (i == 12 and j == 7) or (i == 12 and j == 12) or (i == 9 and j == 16) or (i == 7 and j == 10):
                level[i][j] = 4
                level[i][j+1] = -4
                level[i][j+2] = -4
                counter = 2
            elif(i == 15):
                level[i][j] = 2
            elif(i == 3 and j == 20):
                level[i][j] = 1
                level[i][j+1] = 2
                level[i][j+2] = 2
                level[i][j+3] = 2
                counter = 3
            else:
                level[i][j] = 0
            counter -=1
    return level
#--------------------------

def make_tile_array(tile_size):
    # cropped_image = img.crop((0, 0, 512, 512))
    sprites = []
    width = height = tile_size
    # create an empty image
    img = Image.new("RGBA", (tile_size, tile_size), (255, 255, 255, 255))
    sprites.append(img)
    sprites.append((Image.open('assets/tileset/Ground_Asset_LT.png').crop((0,0,221,221))).resize((tile_size, tile_size)))
    sprites.append((Image.open('assets/tileset/Ground_Asset.png').crop((0,0,221,221))).resize((tile_size, tile_size)))
    sprites.append((Image.open('assets/tileset/Ground_Asset_RT.png').crop((0,0,221,221))).resize((tile_size, tile_size)))
    sprites.append((Image.open('assets/tileset/Platform_Asset.png').crop((0,0,221*3,221))).resize((tile_size*3, tile_size)))
    return sprites
    
# draw the level when screen is passed in
def draw(screen, level):
    tile_size = 50
    tiles = make_tile_array(tile_size)
    for row in range(len(level)):
        for col in range(len(level[row])):
            # Convert the tile to a Pygame Surface object
            tile = tiles[0]
            tile = pygame.image.fromstring(tile.tobytes(), tile.size, tile.mode)
            if level[row][col] > 0:
                tile = tiles[level[row][col]]
                tile = pygame.image.fromstring(tile.tobytes(), tile.size, tile.mode)

                # Calculate the position to draw the tile on the screen
                x = col * tile_size
                y = row * tile_size

                # Draw the tile on the screen
                screen.blit(tile, (x, y))