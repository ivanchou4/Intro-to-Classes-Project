import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, KEYUP, QUIT, MOUSEBUTTONDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

from player import Player

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

player = Player()
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_UP:
                player.pressed_up = True
            if event.key == K_DOWN:
                player.pressed_down = True
            if event.key == K_LEFT:
                player.pressed_left = True
            if event.key == K_RIGHT:
                player.pressed_right = True
                
        elif event.type == KEYUP:
            if event.key == K_UP:
                player.pressed_up = False
            if event.key == K_DOWN:
                player.pressed_down = False
            if event.key == K_LEFT:
                player.pressed_left = False
            if event.key == K_RIGHT:
                player.pressed_right = False

        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            pass

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    #chceks for button clicks and if player has hit a boundry or not
    if player.pressed_up:
        player.move_up(WIDTH, HEIGHT)
    if player.pressed_down:
        player.move_down(WIDTH, HEIGHT)
    if player.pressed_left:
        player.move_left(WIDTH, HEIGHT)
    if player.pressed_right:
        player.move_right(WIDTH, HEIGHT)
            
    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    player.draw(screen)

    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
