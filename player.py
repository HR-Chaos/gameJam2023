# create a player class
import pygame
import autotiler
import numpy as np


class Player:
    inventory = []
    def init_running_frames(self):
        self.running_frames = [pygame.image.load("assets/mushroom/-2.png"), pygame.image.load("assets/mushroom/-1.png"), pygame.image.load("assets/mushroom/0.png"), pygame.image.load("assets/mushroom/1.png"), pygame.image.load("assets/mushroom/2.png")]
        temp = []
        temp.append(self.running_frames[2])
        temp.append(self.running_frames[3])
        temp.append(self.running_frames[4])
        temp.append(self.running_frames[3])
        temp.append(self.running_frames[2])
        temp.append(self.running_frames[1])
        temp.append(self.running_frames[0])
        temp.append(self.running_frames[1])
        self.running_frames = temp
    def __init__(self, img, x, y, speed):
        self.img = img
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.speed = speed
        self.reversed = False
        self.player_state = 0
        self.player_states = ["idle", "run", "jump", "plant"]
        self.init_running_frames()
    def draw(self, screen, player_state):
        if player_state == 0:
            self.img = pygame.image.load("assets/mushroom/idle.png")
        elif player_state == 1:
            self.img = self.running_frames[int(pygame.time.get_ticks()/100)%len(self.running_frames)]
        elif player_state == 2:
            self.img = pygame.image.load("assets/mushroom/0.png")
        elif player_state == 3:
            self.img = pygame.image.load("assets/mushroom/crouch.png")
        if self.dx < 0 or self.reversed == True:
            self.img = pygame.transform.flip(self.img, True, False)
            self.reversed = True
        if self.dx > 0 :
            self.reversed = False
        screen.blit(self.img, (self.x, self.y+5))
        self.player_state = player_state
    def update(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.x += dx
        self.y += dy
    def move(self):
        pass
    def jump(self):
        pass
    def pick_up(self):
        pass
    def plant(item):
        pass
    def get_inventory(self):
        pass
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_speed(self):
        return self.speed
    def get_img(self):
        return self.img
    def get_height(self):
        return self.img.get_height()
    def get_width(self):
        return self.img.get_width()