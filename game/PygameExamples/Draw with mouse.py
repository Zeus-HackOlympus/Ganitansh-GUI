import pygame
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 1920,1080
screen = pygame.display.set_mode((WIDTH,HEIGHT))

OFFWHITE = (251,255,203)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

start = (0,0)
size = (0,0)
drawing = False
running = True




while running :
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0,0
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] -start[0],end[1] - start[1]
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1]-start[1]
    screen.fill(BLACK)

    print(start , size)
    pygame.draw.rect(screen,WHITE,(start,size),2)

    pygame.display.update()



