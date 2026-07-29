import pygame
from time import *

pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))

bg = pygame.image.load("bg.jpg")
ship = pygame.image.load("ship.png")

bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
ship = pygame.transform.scale(ship,(100,100))

ship_x = 100
ship_y = 10

keys = [False,False,False,False]

while ship_y < 400:
    screen.blit(bg,(0,0))
    screen.blit(ship,(ship_x,ship_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            # for when a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0]=True
            if event.key == pygame.K_DOWN:
                keys[2]=True
            if event.key == pygame.K_LEFT:
                keys[1]=True
            if event.key == pygame.K_RIGHT:
                keys[3]=True
            # for when a key is let go
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0]=False
            if event.key == pygame.K_DOWN:
                keys[2]=False
            if event.key == pygame.K_LEFT:
                keys[1]=False
            if event.key == pygame.K_RIGHT:
                keys[3]=False
    if keys [0]:
        if ship_y > 0:
            ship_y -= 7
    if keys [2]:
        if ship_y < 400:
            ship_y += 7
    if keys [1]:
        if ship_x > 0 :
            ship_x -= 7
    if keys [3]:
        if ship_x < 400:
            ship_x += 7
    ship_y += 5
    sleep(0.05)
print("game over!")