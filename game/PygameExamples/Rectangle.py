import pygame
from pygame.locals import  *

pygame.init()

screen = pygame.display.set_mode((800,800))
color = (255,0,0)
rect0 = Rect(0,790,100,10)
rect = rect0.copy()
pygame.display.update()
running = True

while running :
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT :
            running = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                rect.move_ip(5,0)
                pygame.display.update()
            elif event.key == K_LEFT:
                rect.move_ip(-5,0)
                pygame.display.update()
        pygame.draw.rect(screen,color,rect0)
        pygame.draw.rect(screen,color,rect)
        pygame.display.flip()
