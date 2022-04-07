
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
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)


balls = []
squares = []
button = ShapeCreatorButton(20, 20, 150, 50, "ADD", myfont)

player = Player()

# ---------------------------

running = True
while running:
    screen.fill((255, 255, 255))  # always the first drawing command
        # completely fill the surface object
    # with white color

    for ball in balls:
        if ball.x + ball.radius > WIDTH or ball.x - ball.radius < 0:
            ball.dx *= -1
        if ball.y + ball.radius > HEIGHT or ball.y - ball.radius < 0:
            ball.dy *= -1  
        ball.x += ball.dx
        ball.y += ball.dy
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
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
            if button.get_rect().collidepoint(event.pos): 
                random_num = random.randint(1,2)
                if random_num == 1:
                    balls.append(Ball(random.randrange(50, WIDTH-50), random.randrange(50, HEIGHT-50),random.randrange(-5, 5),random.randrange(-5, 5), 40))
                if random_num == 2:
                    squares.append(Square(random.randrange(50, WIDTH-50), random.randrange(50, HEIGHT-50), 5, 5))
                
                print("Button CLicked")
                

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    for square in squares:
        square.move()

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
