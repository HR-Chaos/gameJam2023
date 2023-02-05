import pygame

class Seed:
    def __init__(self, path, x, y):
        self.img = pygame.image.load(path)
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 3
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    def update(self, map, tile_size):
        self.y+=self.dy
        if map[(self.get_y()+1+self.get_height())//tile_size][(self.get_x()+1+self.get_width())//tile_size] != 0 or map[(self.get_y()+1+self.get_height())//tile_size][(self.get_x())//tile_size] != 0:
            if self.dy > 0:
                self.dy = 0
        if map[(self.get_y()-1)//tile_size][(self.get_x()+1+self.get_width())//tile_size] != 0:
            if self.dy < 0:
                self.dy = 0
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def get_img(self):
        return self.img
    def get_height(self):
        return self.img.get_height()
    def get_width(self):
        return self.img.get_width()
    def set_dy(self, dy):
        self.dy = dy