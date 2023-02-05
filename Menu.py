import pygame
import time
import button
# initialize pygame and screen
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH*9/16)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shroomdom")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#game variables
paused = False
running = True
#load images
start = pygame.image.load('start.png').convert_alpha()
exit = pygame.image.load('exit.png').convert_alpha()
start_button = button.Button(550, 200, start)
exit_button = button.Button(550, 400, exit)
#define font
font = pygame.font.SysFont("arialblack", 33)
#define colors
CYAN = (200, 220, 240)
text_col = (255, 255, 255)
screen.fill(CYAN)
pygame.display.update()
while running:
    if start_button.draw(screen):
        #print('Start')
        pass
    if exit_button.draw(screen):
        #print('Exit')
        running = False
    draw_text("Shroomdom", font, text_col, 475, 100)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if paused == False:
                    paused=True
                else:
                    paused=False
        if paused == False:
            pass
            # screen.fill(CYAN)
            # draw_text("Main Menu", font, text_col, 500, 100)
            #draw_text("Press P to play", font, text_col, 444, 300)
            #put stuff to go back to game here
        else:
            pass
            #screen.fill(CYAN)
            #draw_text("Insert Insane Gameplay Here", font, text_col, 400, 100)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()