import pygame

class Circle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.radius = 15
        self.colour = (0, 0, 255)
        self.width = 1

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, self.colour, (self.x, self.y), self.radius, self.width)
