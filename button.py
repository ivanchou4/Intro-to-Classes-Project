import pygame
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
