import random
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

class Ball:
    def __init__(self, x: int, y: int, dx: int, dy: int, radius: int) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        self.color = (r, g, b)

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
        if ball.x + ball.radius > WIDTH or ball.x - ball.radius < 0:
            ball.dx *= -1
        if ball.y + ball.radius > HEIGHT or ball.y - ball.radius < 0:
            ball.dy *= -1  
        ball.x += ball.dx
        ball.y += ball.dy


    screen.fill((255, 255, 255))

    for ball in balls:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)


    pygame.display.flip()
    clock.tick(60)


pygame.quit()
