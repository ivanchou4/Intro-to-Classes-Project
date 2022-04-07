import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, KEYUP, QUIT, MOUSEBUTTONDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT
from ball import Ball
from button import ShapeCreatorButton
from square import Square
from player import Player


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)


balls = []
squares = []
button = ShapeCreatorButton(20, 20, 150, 50, "ADD", myfont)

pressed_up = False
pressed_down = False
pressed_left = False
pressed_right = False

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
                pressed_up = True
            if event.key == K_DOWN:
                pressed_down = True
            if event.key == K_LEFT:
                pressed_left = True
            if event.key == K_RIGHT:
                pressed_right = True

        elif event.type == KEYUP:
            if event.key == K_UP:
                pressed_up = False
            if event.key == K_DOWN:
                pressed_down = False
            if event.key == K_LEFT:
                pressed_left = False
            if event.key == K_RIGHT:
                pressed_right = False

        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if button.get_rect().collidepoint(event.pos): 
                random_num = random.randint(1,2)
                if random_num == 1:
                    balls.append(Ball(random.randrange(50, WIDTH-50), random.randrange(50, HEIGHT-50),random.randrange(-5, 5),random.randrange(-5, 5), 40))
                if random_num == 2:
                    squares.append(Square(random.randrange(50, WIDTH-50), random.randrange(50, HEIGHT-50), 5, 5))
                

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    
    #updates square positions
    for square in squares:
        square.move()

    #updates ball positions
    for ball in balls:
        ball.move(WIDTH, HEIGHT)
        
    #chceks for button clicks, if true, attempt to move the player
    if pressed_up:
        player.move_up(WIDTH, HEIGHT)
    if pressed_down:
        player.move_down(WIDTH, HEIGHT)
    if pressed_left:
        player.move_left(WIDTH, HEIGHT)
    if pressed_right:
        player.move_right(WIDTH, HEIGHT)

    #chceks for player collisions, if true, resets the game
    if player.collision(squares, balls):
        squares = []
        balls = []
        player.x = 100
        player.y = 100
        
    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    player.draw(screen)
    
    for ball in balls:
        ball.draw(screen)

    for square in squares:
        square.draw(screen)

    button.draw(screen)


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
