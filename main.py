import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, KEYUP, QUIT, MOUSEBUTTONDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT
from ball import Ball
from button import ShapeCreatorButton
from square import Square
from player import Player
from projectile import Projectile

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
play_button = ShapeCreatorButton(500, 20, 100, 50, (0, 200, 0), "Play", myfont)
pause_button = ShapeCreatorButton(320, 20, 100, 50,(200, 0, 0), "Pause", myfont)  
button = ShapeCreatorButton(20, 20, 150, 50,(200, 200, 200),  "ADD", myfont)
pause = False
pressed_up = False
pressed_down = False
pressed_left = False
pressed_right = False

player = Player(100, 100, 10, 6)
projectiles = []

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
            if pause_button.get_rect().collidepoint(event.pos):
                pause = True
            if play_button.get_rect().collidepoint(event.pos):
                pause = False

            if button.get_rect().collidepoint(event.pos): 
                random_num = random.randint(1,2)
                if random_num == 1:
                    balls.append(Ball(random.randrange(50, WIDTH-50), random.randrange(50, HEIGHT-50),random.randrange(-5, 5),random.randrange(-5, 5), 40))
                if random_num == 2:
                    squares.append(Square(random.randrange(50, WIDTH-50), random.randrange(50, HEIGHT-50), 5, 5, 20))
                
            else:
                projectiles.append(Projectile(player.x, player.y, 2, event.pos[0], event.pos[1], 10))

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    #updates projectile positions and checks for its collisions
    if pause == False:
        for projectile in projectiles:
            projectile.move()
            for square in squares:
                if projectile.on_hit(square.circle_x, square.circle_y, square.circle_radius):
                    try:
                        squares.remove(square)
                        projectiles.remove(projectile)
                    except ValueError:
                        pass
            for ball in balls: 
                if projectile.on_hit(ball.x, ball.y, ball.radius):
                    try:
                        balls.remove(ball)
                        projectiles.remove(projectile)
                    except ValueError:
                        pass
            
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
            projectiles = []
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

    for projectile in projectiles:
        projectile.draw(screen)

    if len(balls) + len(squares) > 10: 
        pause_button.draw(screen)
        play_button.draw(screen)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
