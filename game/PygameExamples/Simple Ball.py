import random

import pygame
from pygame.locals import  *
pygame.init()


BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

colors = [
    BLACK,
    GRAY,
    WHITE,
    RED,
    GREEN,
    BLUE,
    YELLOW,
    CYAN,
    MAGENTA
]

WIDTH = 1920
HEIGHT = 1080
GREEN = (155,255,150)
RED = (255,0,0)


screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True
ball = pygame.image.load("ball.png")

rect = ball.get_bounding_rect()
speed = [1,1]

while running:
    for event in pygame.event.get():
        if event.type == QUIT :
            running = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > WIDTH:
        speed[0] = -speed[0]
        screen.fill(colors[random.randint(0,len(colors)-1)])
        pygame.display.update()
    if rect.top < 0 or rect.bottom > HEIGHT :
        speed[1] = -speed[1]
        screen.fill(colors[random.randint(0,len(colors)-1)])
        pygame.display.update()

    screen.fill(GREEN)
    pygame.draw.rect(screen,RED,rect,1)
    screen.blit(ball,rect)
    pygame.display.update()

pygame.quit()