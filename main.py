import pygame
import autotiler
import numpy as np
import player
import level_maker
from PIL import Image
import seed
import os

# initialize pygame and screen
pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH*2/3)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("gameJam2023")
run = True
tile_size = player_x = player_y = player_dx = player_dy = 0
tiles = map = []
# player_states = ["idle", "walk", "jump", "fall", "attack", "hurt", "dead"]
IDLE_STATE = 0
WALK_STATE = 1
JUMP_STATE = 2
FALL_STATE = 3
ATTACK_STATE = 4
player_state = IDLE_STATE

door_img = pygame.image.load('assets\seed_animations\Door.png')
rect = pygame.Rect(0, 0, 335, 357)
door_img = door_img.subsurface(rect)
door_img = pygame.transform.scale(door_img, (175, 175))
background_img = pygame.image.load('assets\Game_Background_Base.png')
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

path_animations = 'assets\seed_animations'
# for every png in the folder, add it to the list
seed_animation = [pygame.image.load(path_animations + '\\' + img) for img in os.listdir(path_animations) if img.endswith(".png")]
for i in range(len(seed_animation)):
    rect = pygame.Rect(0, 0, 489, 634)
    cropped_image = seed_animation[i].subsurface(rect)
    seed_animation[i] = pygame.transform.scale(cropped_image, (150, 400))
animation_index = 0
planted = False

# initialize player
player_img = pygame.image.load('assets/adventurer/adventurer-idle-00.png')
# change player image to directory
p = player.Player(player_img, 100, 400, 5)
# img = pygame.image.load("player.png")
seed1 = seed.Seed("assets\seeds\Everbloom_seed.png", 500, 200)

tile_size = 50

tiles = autotiler.make_tile_array(tile_size)
map = level_maker.get_level_1()
level = level_maker.get_level_1()

def draw_map(screen, map):
    level_maker.draw(screen, level)

def draw_player(screen, x, y, player_state):
    # screen.blit(img, (x, y))
    p.draw(screen, player_state)

def draw_background(screen, map):
    screen.blit(background_img, (0, 0))

def draw_seed_animation(screen, p):
    global animation_index
    while animation_index < len(seed_animation):
        screen.blit(seed_animation[animation_index], (p.get_x()+50, p.get_y()))
        animation_index += 1
        print('index: ', animation_index)
        pygame.time.delay(100)

while run:
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
        player_dx -=2
        if player_dx < -10:
            player_dx = -10
    if keys[pygame.K_d]:
        player_dx += 2
        if player_dx > 10:
            player_dx = 10
    if keys[pygame.K_w] and player_state != JUMP_STATE and player_state != FALL_STATE:
        player_dy -= 20
        if player_dy < -20:
            player_dy = -20
    
    # gravity
    player_dy += 1
    if player_dy > 25:
        player_dy = 25
    
    #check player collision with map
    if planted:
        temp_rect = pygame.Rect(p.get_x(), p.get_y(), p.get_width(), 30)
        leaf_rect = pygame.Rect(loc_x, loc_y+50, 150, 10)
        if temp_rect.colliderect(leaf_rect):
            if player_dy > 0:
                player_dy = 0
                player_state = IDLE_STATE
    if map[(p.get_y()+1+p.get_height())//tile_size][(p.get_x()+1+p.get_width())//tile_size] != 0 or map[(p.get_y()+1+p.get_height())//tile_size][(p.get_x())//tile_size] != 0:
        if player_dy > 0:
            player_dy = 0
    if map[(p.get_y()-1)//tile_size][(p.get_x()+1+p.get_width())//tile_size] != 0:
        if player_dy < 0:
            player_dy = 0

    draw_background(screen, map)
    screen.blit(door_img, (1025, 0))
    if keys[pygame.K_s]:
        player_state = 3
        rect1 = pygame.Rect(p.get_x(), p.get_y(), p.get_width(), p.get_height())
        rect2 = pygame.Rect(seed1.get_x(), seed1.get_y(), seed1.get_width(), seed1.get_height())
        if rect1.colliderect(rect2):
            seed1.set_x(20)
            seed1.set_y(20)
            seed1.set_dy(0)
            p.set_holding(0, True)
    elif keys[pygame.K_x]:
        player_state = 3
        planted = True
        if p.get_holding(1):
            p.set_holding(1, False)
            loc_x = p.get_x()
            loc_y = p.get_y() + p.get_height() - seed_animation[10].get_height() + 10
            # draw_seed_animation(screen, p)
            print("seed planted")
    elif player_dx == 0 and player_dy == 0 and map[(p.get_y()+1+p.get_height())//tile_size][p.get_x()//tile_size] != 0:
        player_state = IDLE_STATE
    elif player_dx != 0 and map[(p.get_y()+1+p.get_height())//tile_size][p.get_x()//tile_size] != 0:
        player_state = WALK_STATE
    elif player_dy < 0:
        player_state = JUMP_STATE
    elif player_dy > 0:
        player_state = FALL_STATE
    
    # update seeds

    draw_map(screen, map)  
    p.update(player_dx, player_dy)
    seed1.update(map, tile_size)
    seed1.draw(screen)
    draw_player(screen, player_x, player_y, player_state)
    if planted:
        screen.blit(seed_animation[10], (loc_x, loc_y))
    # update display
    pygame.display.update()
    
pygame.quit()
quit()