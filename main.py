import pygame
import autotiler
import numpy as np
import player
import level_maker
import button
import time

# initialize pygame and screen
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH*2/3)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shroomdom")
run = True
tile_size = player_x = player_y = player_dx = player_dy = 0
tiles = map = []
player_states = ["idle", "walk", "jump", "fall", "attack", "hurt", "dead"]
IDLE_STATE = 0
WALK_STATE = 1
JUMP_STATE = 2
FALL_STATE = 3
ATTACK_STATE = 4
HURT_STATE = 5
DEAD_STATE = 6
player_state = IDLE_STATE
game_state = 0

# initialize player
player_img = pygame.image.load('assets/adventurer/adventurer-idle-00.png')
# change player image to directory
p = player.Player(player_img, 100, 400, 5)
# img = pygame.image.load("player.png")

tile_size = 50

tiles = autotiler.make_tile_array(tile_size)
map = level_maker.get_level_1()

def draw_map(screen, map):
    screen.fill((0, 0, 0))
    level = level_maker.get_level_1()
    level_maker.draw(screen, level)
    # screen.fill((255, 255, 255))
    # for row in range(len(map)):
    #     for col in range(len(map[row])):
    #         # Convert the tile to a Pygame Surface object
    #         tile = tiles[map[row][col]]
    #         tile = pygame.image.fromstring(tile.tobytes(), tile.size, tile.mode)

    #         # Calculate the position to draw the tile on the screen
    #         x = col * tile_size
    #         y = row * tile_size

    #         # Draw the tile on the screen
    #         screen.blit(tile, (x, y))

def draw_player(screen, x, y, player_state):
    # screen.blit(img, (x, y))
    p.draw(screen, player_state)

#helper function for def start_menu
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def start_menu():
    start_menu_game_state = 0
    #load images
    start = pygame.image.load('assets\start.png').convert_alpha()
    exit = pygame.image.load('assets\exit.png').convert_alpha()
    start_button = button.Button(550, 200, start)
    exit_button = button.Button(550, 400, exit)
    #define font
    font = pygame.font.SysFont("arialblack", 33)
    #define color of text
    text_col = (255, 255, 255)

    if start_button.draw(screen):
        print("You clicked start")
        start_menu_game_state = 1
        pass
    if exit_button.draw(screen):
        print("You c`licked exit")
        pygame.quit()
    
    draw_text("Shroomdom", font, text_col, 475, 100)
    pygame.display.update()

    return start_menu_game_state

while run:

    if game_state == 0:
        game_state = start_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    elif game_state == 1:
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
            # keypresses

        keys = pygame.key.get_pressed()  #checking pressed keys
        # if key not pressed, reset player speed
        if sum(keys) == 0:
            if player_dx > 0:
                player_dx -= 2
                if player_dx < 0:
                    player_dx = 0
            if player_dx < 0:
                player_dx += 2
                if player_dx > 0:
                    player_dx = 0

        if keys[pygame.K_a]:
            player_dx -=1
            if player_dx < -10:
                player_dx = -10
        if keys[pygame.K_d]:
            player_dx += 1
            if player_dx > 10:
                player_dx = 10
        if keys[pygame.K_w] and player_state != JUMP_STATE and player_state != FALL_STATE:
            player_dy -= 15
        if keys[pygame.K_s]:
            pass
        
        # gravity
        player_dy += 1
        if player_dy > 25:
            player_dy = 25
        
        #check player collision with map
        if map[(p.get_y()+1+p.get_height())//tile_size][(p.get_x()+1+p.get_width())//tile_size] != 0 or map[(p.get_y()+1+p.get_height())//tile_size][(p.get_x())//tile_size] != 0:
            if player_dy > 0:
                player_dy = 0
        if map[(p.get_y()-1)//tile_size][(p.get_x()+1+p.get_width())//tile_size] != 0:
            if player_dy < 0:
                player_dy = 0

        #update player state
        if player_dx == 0 and player_dy == 0 and map[(p.get_y()+1+p.get_height())//tile_size][p.get_x()//tile_size] != 0:
            player_state = IDLE_STATE
        elif player_dx != 0 and map[(p.get_y()+1+p.get_height())//tile_size][p.get_x()//tile_size] != 0:
            player_state = WALK_STATE
        elif player_dy < 0:
            player_state = JUMP_STATE
        elif player_dy > 0:
            player_state = FALL_STATE

        draw_map(screen, map)  
        p.update(player_dx, player_dy)
        draw_player(screen, player_x, player_y, player_state)

        # update display
        pygame.display.update()
    
pygame.quit()
quit()