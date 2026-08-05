import pygame
from time import *
from random import randint

pygame.init()
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
bg = pygame.image.load("background.webp")
basket = pygame.image.load("basket.png")
apple = pygame.image.load("apple.png")

# Scale images
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
basket = pygame.transform.scale(basket, (100, 100))
apple = pygame.transform.scale(apple, (50, 50))

# Starting positions
basket_x = 200
basket_y = 400
apple_x = randint(0, WIDTH - 50)
apple_y = 10

# Key tracking
keys = [False, False, False, False]  # [UP, LEFT, DOWN, RIGHT]

# Game loop
while True:
    screen.blit(bg, (0, 0))
    screen.blit(basket, (basket_x, basket_y))
    screen.blit(apple, (apple_x, apple_y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            if event.key == pygame.K_LEFT:
                keys[1] = True
            if event.key == pygame.K_DOWN:
                keys[2] = True
            if event.key == pygame.K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            if event.key == pygame.K_LEFT:
                keys[1] = False
            if event.key == pygame.K_DOWN:
                keys[2] = False
            if event.key == pygame.K_RIGHT:
                keys[3] = False

    # Basket movement
    if keys[0] and basket_y > 0:
        basket_y -= 7
    if keys[2] and basket_y < HEIGHT - 100:
        basket_y += 7
    if keys[1] and basket_x > 0:
        basket_x -= 7
    if keys[3] and basket_x < WIDTH - 100:
        basket_x += 7

    apple_y += 5

    if (basket_x < apple_x + 50 and basket_x + 100 > apple_x and
        basket_y < apple_y + 50 and basket_y + 100 > apple_y):
        print("Apple caught!")
        apple_x = randint(0, WIDTH - 50)
        apple_y = 10  # reset apple to top

    if apple_y > HEIGHT - 50:
        print("Game Over!")
        break

    sleep(0.05)
