# pygame template
import random

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

class Ball:
    def __init__(self, x: int, y: int, dx: int, dy: int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        r = random.randrange(0, 256,)
        g = random.randrange(0, 256,)
        b = random.randrange(0, 256,)
        self.color = (r, g, b)

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

balls = [
]

for _ in range(10):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    dx = random.randrange(-5, 5)
    dy = random.randrange(-5, 5)
    b = Ball(x, y, dx, dy)
    balls.append(b)
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
    for ball in balls:
        if ball.x > WIDTH or ball.x < 0:
            ball.dx *= -1
        if ball.y > HEIGHT or ball.y < 0:
            ball.dy *= -1  
        ball.x += ball.dx
        ball.y += ball.dy

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    for ball in balls:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), 30)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)
    #---------------------------


pygame.quit()
