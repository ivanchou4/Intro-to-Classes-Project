import pygame
import math

class Projectile:
    def __init__(self, x: int, y: int, radius: int, x_end: int, y_end: int, speed: int) -> None:
        """Constructs attributes related to the class, runs when an instance of this class has been made

        Args:
            x: The projectile's x position
            y: The projectile's y position
            radius: The projectile's circle radius
            x_end: The end destination of the projectile's x value
            y_end: The end destination of the projectile's y value
            speed: The speed of the projectile

        Returns:
            None
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.unit_vector = ((x_end - x)/math.sqrt((x_end - x)**2 + (y_end - y)**2), (y_end - y)/math.sqrt((x_end - x)**2 + (y_end - y)**2))
        self.speed_multiplier = speed

    def move(self) -> None:
        """Updates the Projectile's x and y positions

        Args:
            None

        Returns:
            None
        """
        self.x += self.speed_multiplier * self.unit_vector[0]
        self.y += self.speed_multiplier * self.unit_vector[1]

    def on_hit(self, circle_x, circle_y, circle_radius) -> bool:
        """Detects if the projectile's circle has hit the circle hitbox given in the parameters

        Args:
            circle_x = Circle hitbox's x position
            circle_y = Circle hitbox's y position
            circle_radius = Circle hitbox's radius

        Returns:
            True if the projectile hits the hitbox. False otherwise
        """
        distance = math.sqrt((circle_x - self.x)**2 + (circle_y - self.y)**2)
        if distance < circle_radius + self.radius:
            return True
        return False
            
    def draw(self, surface: pygame.Surface) -> None:
        """Draws the player's circle onto the screen

        Args:
            surface: A pygame surface

        Returns:
            None
        """
        pygame.draw.circle(surface, (0,0,10), (self.x,self.y), self.radius)
