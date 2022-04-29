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

    def move(self, WIDTH: int, HEIGHT: int) -> None:
        """Reverses the direction of the ball/circle object when it hits the width and height of the display window  
        
        Args:
            WIDTH: display window width
            HEIGHT: display window height 
        
        Returns:
            None
        """
        if self.x + self.radius > WIDTH or self.x - self.radius < 0:
            self.dx *= -1
        if self.y + self.radius > HEIGHT - 100 or self.y - self.radius < 0:
            self.dy *= -1  
        self.x += self.dx
        self.y += self.dy
