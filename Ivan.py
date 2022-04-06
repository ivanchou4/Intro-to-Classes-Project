import pygame
import random
class ShapeCreatorButton:
    def __init__(self, x: int, y: int, w: int, h: int):
        print("Creating a button")
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def draw(self, surface: pygame.Surface): 
        pygame.draw.rect(surface, (200, 200, 200), (self.x, self.y, self.width, self.height),0, 100)

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

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

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


    



import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN


pygame.init()

WIDTH = 640
HEIGHT = 450
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

random_num = random.randint(1,1)
balls = [

]

for _ in range(2):
    x = random.randrange(50, WIDTH-50)
    y = random.randrange(50, HEIGHT-50)
    dx = random.randrange(-5, 5)
    dy = random.randrange(-5, 5)
    radius = 40
    b = Ball(x, y, dx, dy, radius)
    balls.append(b)

button = ShapeCreatorButton(50, 50, 150, 50)
# ---------------------------

running = True
while running:
    screen.fill((255, 255, 255))  # always the first drawing command
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
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if button.get_rect().collidepoint(event.pos): 
                balls.append(Ball(random.randrange(50, WIDTH-50), random.randrange(50, HEIGHT-50),random.randrange(-5, 5),random.randrange(-5, 5), 40))
                    
                    
                print("Button CLicked")
                
    
    # GAME STATE UPDATES



    # All game math and comparisons happen here

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command

    for ball in balls:
        ball.draw(screen)

    button.draw(screen)


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
