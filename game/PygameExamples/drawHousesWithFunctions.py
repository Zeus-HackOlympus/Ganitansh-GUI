# drawHousesWithFunctions.py   Draw some houses on the screen (using functions)
# P. Conrad for CS5nm, 10/06/2008


# stuff we need to import in order to use PyGame

import pygame
from pygame.locals import *
from sys import exit

# a function to draw a house with PyGame
# consumes:
#     x, y  (numbers: lower left corner of the house)
#     width, height  (numbers: width and height of house)
#     screen (the screen where we should draw this house)
#     color (a tuple of (r, g, b) representing a color)
# produces
#     nothing
# side effect
#     draws a house on the screen of the size and color given,
#     at the location given

# Note: defining the function does NOT draw ANYTHING
# It is just a "recipe" or a "blueprint" for drawig a house
# The house only gets drawn when we "call" the function with "arguments".

def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height), 
                  (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)



# set up a window (a.k.a. a screen)

size = width, height = 640,480
pygame.init()
screen = pygame.display.set_mode(size)

# set up variables for colors

red = (255, 0, 0 )  # an RGB 3-tuple representing red
green = (0, 255, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# main loop

while True: # loop forever (or at least until someone generates a QUIT event)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); exit()

    screen.fill(white); # Make the whole screen white

    # Now, draw three houses
    
    drawHouse(100,200,120,150,screen,red) 
    drawHouse(400,200,120,150,screen,green) 
    drawHouse(400,400,120,150,screen,blue) 

    # But, we don't actually SEE the houses until we call "update".
    pygame.display.update()
