import pygame
import time
# initialize pygame and screen
pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH*9/16)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pause page")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
#game variables
paused = False
running = True
#define font
font = pygame.font.SysFont("arialblack", 33)
#define colors
GREEN = (0, 255, 0)
text_col = (255, 255, 255)
screen.fill(GREEN)
pygame.display.update()
# pygame.draw.rect(screen, RED, rect, 1)
# if event.type == pygame.KEYDOWN:
#     if event.key == pygame.K_r:
#         background = RED
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if paused == False:
                    paused=True
                else:
                    paused=False
        if paused == False:
            screen.fill(GREEN)
            #put stuff to go back to game here
        else:
            draw_text("Game Paused", font, text_col, 500, 100)
            draw_text("Press R to resume", font, text_col, 444, 300)
        if event.type == pygame.QUIT:
            #time.sleep(10000)
            running = False
    pygame.display.update()
pygame.quit()