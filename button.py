import pygame

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

