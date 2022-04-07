import random
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from ball import Ball

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


balls = [
]

for _ in range(10):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    dx = random.randrange(-5, 5)
    dy = random.randrange(-5, 5)
    radius = 40
    b = Ball(x, y, dx, dy, radius)
    balls.append(b)


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    
    for ball in balls:
        ball.move(WIDTH, HEIGHT)


    screen.fill((255, 255, 255))

    for ball in balls:
        ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
