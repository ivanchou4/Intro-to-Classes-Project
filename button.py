import pygame
class ShapeCreatorButton:
    def __init__(self, x: int, y: int, w: int, h: int, text: str, font):
        print("Creating a button")
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.text = font.render(text, False, (0,0,0))

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (200, 200, 200), (self.x, self.y, self.width, self.height),0, 100)
        text_rect = self.text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        surface.blit(self.text, text_rect)

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

