import pygame
import random
from pygame.locals import K_ESCAPE, KEYDOWN, KEYUP, QUIT, MOUSEBUTTONDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_r
from ball import Ball
from button import ShapeCreatorButton
from player import Player
from user_interface import UserInterface

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
ui = UserInterface(0, HEIGHT - 100, WIDTH, 100, (100, 50, 0), myfont, screen)
pause = False
pressed_up = False
pressed_down = False
pressed_left = False
pressed_right = False

player = Player(100, 100, 10, 6)
bullets = []

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
            if event.key == K_r:
                player.gun.reload()
        
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
            if ui.pause_button.get_rect().collidepoint(event.pos):
                pause = True
            elif ui.play_button.get_rect().collidepoint(event.pos):
                pause = False
            elif ui.button.get_rect().collidepoint(event.pos):
                balls.append(Ball(random.randrange(50, WIDTH-50), random.randrange(50, HEIGHT-150),random.randrange(-5, 5),random.randrange(-5, 5), 40))
            elif ui.get_rect().collidepoint(event.pos):
                pass
            else:
                if player.gun._magazine_bullets > 0:   
                    bullets.append(player.gun.shoot(player.x, player.y, event.pos[0], event.pos[1]))

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    #updates bullet positions and checks for its collisions
    if pause == False:
        for bullet in bullets:
            bullet.move()
            for ball in balls: 
                if bullet.on_hit(ball.x, ball.y, ball.radius):
                    player.gun.set_bullets(player.gun.get_bullets() + 1)
                    try:
                        balls.remove(ball)
                        bullets.remove(bullet)
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
            
        #checks for player collisions, if true, resets the game
        if player.collision(squares, balls):
            squares = []
            balls = []
            bullets = []
            player = Player(100, 100, 10, 6)
    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    player.draw(screen)
    
    for ball in balls:
        ball.draw(screen)

    for square in squares:
        square.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    ui.draw(player.gun.get_bullets(), player.gun.get_magazine_capacity(), player.gun.get_magazine_bullets(), myfont)
    
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
