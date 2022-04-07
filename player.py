import pygame
import math

class Player:
    def __init__(self):
        self.x= 100
        self.y = 100
        self.radius = 10
        self.speed = 6
        self.pressed_up = False
        self.pressed_left = False
        self.pressed_right = False
        self.pressed_down = False
        self.invulnerable = False
    
    def move_up(self, width, height):
        if self.y - self.radius >= 0:
            self.y -= self.speed
    def move_down(self, width, height):
        if self.y + self.radius <= height:
            self.y += self.speed
    def move_left(self, width, height):
        if self.x - self.radius >= 0:
            self.x -= self.speed
    def move_right(self, width, height):
        if self.x + self.radius <= width:
            self.x += self.speed

    def on_collision(self, squares, circles):
        for ball in balls:
            distance = math.sqrt((ball.x - self.x)**2 + (ball.y - self.y)**2)
            if distance < ball.radius + self.radius:
                return True
            
    
    def draw(self, surface):        
        pygame.draw.circle(surface, (0,0,10), (self.x,self.y), self.radius)





# def dist_2_points(x1, y1, x2, y2):
#     return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# def detect_collision(distance, circle_r1, circle_r2):
#     return distance < circle_r1 + circle_r2
