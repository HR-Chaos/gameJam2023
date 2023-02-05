import pygame
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.image = pygame.transform.scale(image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self, page):
        action = False
        #gets mouse pos
        pos = pygame.mouse.get_pos()
        #print(pos)
        #check click button
        if self.rect.collidepoint(pos):
            #print('Hover')
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                #print('CLICKED')
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        #draws button
        page.blit(self.image, (self.rect.x, self.rect.y))
        return action