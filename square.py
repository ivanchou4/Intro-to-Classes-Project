import pygame

class Square:
    def __init__(self, x:int, y:int, speed_x: int, speed_y: int, size: int): 
        self.x = x
        self.y = y
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.circle_x = x + self.size/2
        self.circle_y = y + self.size/2
        self.circle_radius = self.size/2
    
    def move(self) -> None:
        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.x < 0 or self.x > 640:
            self.speed_x *= -1
        if self.y < 0 or self.y > 480:
            self.speed_y *= -1

        self.circle_x = self.x + self.size/2
        self.circle_y = self.y + self.size/2
        
        
    def draw(self, surface) -> None:
        pygame.draw.rect(surface, (0, 0, 200), (self.x, self.y, self.size, self.size))
