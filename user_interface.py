import pygame
from button import ShapeCreatorButton

class UserInterface:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, font, surface: pygame.surface):
        self.rect = pygame.Rect(x, y, width, height)
        self.surface = surface
        self.color = color
        self.play_button = ShapeCreatorButton(265, 410, 100, 50, (0, 200, 0), "Play", font)
        self.pause_button = ShapeCreatorButton(375, 410, 100, 50,(200, 0, 0), "Pause", font)
        self.button = ShapeCreatorButton(485, 410, 150, 50,(200, 200, 200),  "ADD", font)

    def get_rect(self):
        return self.rect
    
    def draw(self, bullets, magazine_capacity, magazine_bullets, font):
        #brown box
        pygame.draw.rect(self.surface, self.color, self.rect)

        #buttons
        self.play_button.draw(self.surface)
        self.pause_button.draw(self.surface)
        self.button.draw(self.surface)

        #bullets left
        self.ui_bullets = font.render(str(bullets), False, (255, 255, 255))
        self.surface.blit(self.ui_bullets, (20, 425))

        #magazine
        i = 0
        for num in range(0, magazine_bullets):
            pygame.draw.circle(self.surface, (0, 0, 0), (110 + i, 435), 10)
            i += 25
