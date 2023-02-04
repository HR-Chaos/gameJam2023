import pygame
import autotiler
import numpy as np

# initialize pygame and screen
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH*9/16)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("gameJam2023")
run = True

# initialize location of player
x = 200
y = 200
# img = pygame.image.load("player.png")

tile_size = 50
columns = 7
rows = 7
tiles = autotiler.make_tile_array(tile_size)
map = autotiler.make_map()

def draw_map(screen, map):
    screen.fill((255, 255, 255))
    for row in range(7):
        for col in range(7):
            # Convert the tile to a Pygame Surface object
            tile = tiles[map[row][col]]
            tile = pygame.image.fromstring(tile.tobytes(), tile.size, tile.mode)

            # Calculate the position to draw the tile on the screen
            x = col * tile_size
            y = row * tile_size

            # Draw the tile on the screen
            screen.blit(tile, (x, y))
    
while run:
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
          
    draw_map(screen, map)  
    # update display
    pygame.display.update()
    
pygame.quit()
quit()