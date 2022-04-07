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

    def collision(self, squares, balls):
        for ball in balls:
            distance = math.sqrt((ball.x - self.x)**2 + (ball.y - self.y)**2)
            if distance < ball.radius + self.radius:
                return True
        for square in squares:
            square_radius = square.size/2
            distance = math.sqrt(((square.x + square_radius) - self.x)**2 + ((square.y + square_radius) - self.y)**2)
            if distance < square_radius + self.radius:
                return True
            
    def draw(self, surface):        
        pygame.draw.circle(surface, (0,0,10), (self.x,self.y), self.radius)
