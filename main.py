import pygame

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
img = pygame.image.load("player.png")

while run:
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
            
    # update display
    pygame.display.update()
    
pygame.quit()
quit()