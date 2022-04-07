import random
import pygame

class Ball:
    def __init__(self, x: int, y: int, dx: int, dy: int, radius: int) -> None:
        """Stores values for the ball/circle object
        
        Args:
            x: x location
            y: y location
            dx: x speed
            dy: y speed
            radius: radius
        
        Returns:
            None        
        """
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        self.color = (r, g, b)

    def draw(self, surface: pygame.Surface) -> None:
        """Allows the ball/circle object to be drawn with specific values  
        
        Args:
            surface: pygame.Surface
        
        Returns:
            None
        """
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
