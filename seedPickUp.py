import pygame
import time
import os
import math

VIOLET_RED = (204,0,136)

#Initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
screen.fill(VIOLET_RED)
pygame.display.set_caption("Opening Window")
icon = pygame.image.load('Spring2023Calendar.png')
pygame.display.set_icon(icon)
pygame.display.update()

#Player
playerImg = pygame.image.load('andreiTarkovskyTextsStanleyKubrick.png')
#changes size of image
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

#---------------------------------------------------------------------------------------
#Seed
seedImg = pygame.image.load('placeholderSeed.png')
#changes size of image
seedImg = pygame.transform.scale(seedImg, (20, 20))
seedX = 400
seedY = 400
seedX_change = 0
seedY_change = 0
seed_state = "Dormant"

def seed(x, y):
    if seed_state != "Picked Up":
        screen.blit(seedImg, (x, y))
#---------------------------------------------------------------------------------------------

#Game Loop
running = True
clock = pygame.time.Clock()

def pickUpSeed(playerX, playerY, seedX, seedY):
    distance = math.sqrt(math.pow(playerX - seedX, 2) + math.pow(playerY - seedY, 2))
    if distance < 50: # instead of 50, use size of player character
        return True
    else:
        return False
        

while running:
    clock.tick(60)
    screen.fill(VIOLET_RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -4
            if event.key == pygame.K_d:
                playerX_change = 4
            if event.key == pygame.K_w:
                playerY_change = -4
            if event.key == pygame.K_s:
                playerY_change = 4
#----------------------------------------------------------------------------------
            if event.key == pygame.K_j:
                if pickUpSeed(playerX, playerY, seedX, seedY):
                    seed_state = "Picked Up"
                    #seed is now in pc's inventory
            if event.key == pygame.K_k:
                seed_state = "Planted"
                seedX = playerX + 15
                seedY = playerY + 30
#------------------------------------------------------------------------------------
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
        
        playerX = playerX + playerX_change
        playerY = playerY + playerY_change
        
        if playerX <= 0:
            playerX = 0
        elif playerX >= 780:
            playerX = 780
        if playerY <= 0:
            playerY = 0
        elif playerY >= 580:
            playerY = 580

    player(playerX,playerY)
 #--------------------------------------------------------------------------------
    seed(seedX, seedY)
#--------------------------------------------------------------------------------
    pygame.display.update()

pygame.quit()