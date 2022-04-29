import pygame

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
        self.surface.blit(font.render(str(bullets), False, (255, 255, 255)), (20, 425))

        #magazine
        self.offset = 0
        for num in range(0, magazine_bullets):
            pygame.draw.circle(self.surface, (0, 0, 0), (100 + self.offset, 435), 10)
            self.offset += 25

        #helper text
        self.surface.blit(font.render("R to reload", False, (255, 255, 255)), (97, 455))

class ShapeCreatorButton:
    def __init__(self, x: int, y: int, w: int, h: int, colour: tuple, text: str, font):
        """Initialize the button and text dimensions and location
        Args:
            x (int): x location of button
            y (int): y location of button
            w (int): width of button
            h (int): height of button
            text (str): text of the button
            font (_type_): type of font used
        
        Returns:
            None
        """
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.colour = colour
        self.text = font.render(text, False, (0,0,0))

    def draw(self, surface: pygame.Surface) -> None:
        """Draws the button and Text on the surface
        Args:
            surface (pygame.Surface): Screen where the button and text is drawn
        Returns: 
            None
        """
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height),0, 100)
        text_rect = self.text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        surface.blit(self.text, text_rect)

    def get_rect(self) -> pygame.Rect:
        """Returns Button Object dimensions and location
        Returns:
            pygame.Rect: dimensions and locations of the buttons
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)
