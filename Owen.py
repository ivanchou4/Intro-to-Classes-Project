
# pygame template

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from square import Square
from random import randrange
pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
x = 300
y = 300
square = Square(x,y,5,7)

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    square.move()
   

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command
    square.draw(screen)
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
