import random
import pygame

class Ball(object):
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
        self._x = x
        self._y = y
        self._dx = dx
        self._dy = dy
        self._radius = radius
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        self._color = (r, g, b)

    def draw(self, surface: pygame.Surface) -> None:
        """Allows the ball/circle object to be drawn with specific values  
        
        Args:
            surface: pygame.Surface
        
        Returns:
            None
        """
        pygame.draw.circle(surface, self._color, (self._x, self._y), self._radius)
  
    def move(self, width: int, height: int) -> None:
        """Reverses the direction of the ball/circle object when it hits the width and height of the display window  
        
        Args:
            width: display window width
            height: display window height 
        
        Returns:
            None
        """
        if self._x + self._radius > width or self._x - self._radius < 0:
            self._dx *= -1
        if self._y + self._radius > height + 100 or self._y - self._radius < 0:
            self._dy *= -1  
        self._x += self._dx
        self._y += self._dy

class BossBall(object):
    def __init__(self, x: int, y: int, dx: int, dy: int, radius: int, current_health: int) -> None:
        """Stores values for the bossball/circle object
        
        Args:
            x: x location
            y: y location
            dx: x speed
            dy: y speed
            radius: radius
        
        Returns:
            None        
        """
        self._x = x
        self._y = y
        self._dx = dx
        self._dy = dy
        self._radius = radius
        self._color = (136, 8, 8)
        self._healthbar = HealthBar(current_health)
    
    def draw(self, surface: pygame.Surface) -> None:
        """Allows the bossball/circle object to be drawn with specific values  
        
        Args:
            surface: pygame.Surface
        
        Returns:
            None
        """
        pygame.draw.circle(surface, self.color, (self._x, self._y), self._radius)
  
    def move(self, width: int, height: int) -> None:
        """Reverses the direction of the ball/circle object when it hits the width and height of the display window  
        
        Args:
            width: display window width
            height: display window height 
        
        Returns:
            None
        """
        if self._x + self._radius > width or self._x - self._radius < 0:
            self.dx *= -1
        if self._y + self._radius > height + 100 or self._y - self._radius < 0:
            self._dy *= -1  
        self._x += self._dx
        self._y += self._dy

    def get_healthbar(self) -> int:
        return self._healthbar

    def set_healthbar(self, amount) -> None:
        if self._current_health > 0:
            self._healthbar.damage
        if self._current_health < 0:
            raise ValueError()

class HealthBar:
    def __init__(self) -> None:
        self._current_health = 3
        self._maximum_health = 3
        self._health_bar_length = 50
        self._health_ratio = self._maximum_health / self._health_bar_length

    def update(self):
        self._basic_health()
    
    def damage(self, amount):
        if self._current_health > 0:
            self._current -= amount

    def basic_health(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255, 0, 0), (10, 10, self._current_health / self._health_ratio, 25))
        pygame.draw.rect(surface, (255, 255, 255), (10, 10, self._health_bar_length, 25), 4)
