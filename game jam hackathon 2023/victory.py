import pygame
import time
import button
# initialize pygame and screen
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH*9/16)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Victory!!!")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#game variables
paused = False
running = True
#load images
restart = pygame.image.load('recycle.png').convert_alpha()
restart_button = button.Button(500, 200, restart)
sus = pygame.image.load('sus.png').convert_alpha()
sus_button = button.Button(350, 200, sus)
sus2 = pygame.image.load('sus.png').convert_alpha()
sus_button2 = button.Button(650, 200, sus)
#define font
font = pygame.font.SysFont("arialblack", 33)
#define colors
CYAN = (200, 220, 240)
text_col = (255, 255, 0)
screen.fill(CYAN)
pygame.display.update()
while running:
    if restart_button.draw(screen):
        print('Restart')
        pass
    if sus_button.draw(screen):
        print('ඞ ඞ ඞ ඞ ඞ')
        #draw_text("ඞ ඞ ඞ ඞ ඞ", font, text_col, 500, 300)
        pass
    if sus_button2.draw(screen):
        print('ඞ ඞ ඞ ඞ ඞ')
        #draw_text("ඞ ඞ ඞ ඞ ඞ", font, text_col, 500, 400)
        pass
        #running = False
    draw_text("!!!Victory!!!", font, text_col, 500, 100)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if paused == False:
                    paused=True
                else:
                    paused=False
        if paused == False:
            pass
        else:
            pass
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()