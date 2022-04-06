import pygame

class Player:
    def __init__(self):
        self.x= 100
        self.y = 100
        self.radius = 10
        self.speed = 5
        self.pressed_up = False
        self.pressed_left = False
        self.pressed_right = False
        self.pressed_down = False
        self.invulnerable = False

    
    def move_up(self):
        self.y -= self.speed
    def move_down(self):
        self.y += self.speed
    def move_left(self):
        self.x -= self.speed
    def move_right(self):
        self.x += self.speed

    def on_collision(self):
        #on collision: reset game (remove items fomr balls and squares list, reset player position) ONLY IF PLAYER IS NOT INVULNERABLE
        pass

    def invulnerable(self):
        self.invulnerable = True
    
    def draw(self, surface):        
        pygame.draw.circle(surface, (0,0,10), (self.x,self.y), self.radius)





# def dist_2_points(x1, y1, x2, y2):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# def detect_collision(distance, circle_r1, circle_r2):
#     return distance < circle_r1 + circle_r2
