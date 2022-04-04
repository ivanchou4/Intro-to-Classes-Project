#TEMPLATE FOR SQUARE CLASS
import pygame

class Square:
    def __init__(self, x:int, y:int): 
        self.x = x
        self.y = y
        self.size = 10
        
    def move(self) -> None:
        pass
        
    def draw(self, surface) -> None:
        pygame.draw.rect(surface, (0, 0, 200), (self.x, self.y, self.size, self.size))
