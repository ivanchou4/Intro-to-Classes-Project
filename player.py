import pygame
import math


class Player:
    def __init__(self):
        """Constructs attributes related to the class, runs when an instance of this class has been made

        Args:
            None
        """
        self.x= 100
        self.y = 100
        self.radius = 10
        self.speed = 6
        self.pressed_up = False
        self.pressed_left = False
        self.pressed_right = False
        self.pressed_down = False
        self.invulnerable = False
    
    def move_up(self, width: int, height: int) -> None:
        """Moves the player's circle up
        
        Args:
            width: display window width
            height: display window height

        Returns:
            None
        """
        if self.y - self.radius >= 0:
            self.y -= self.speed
            
    def move_down(self, width: int, height: int) -> None:
        """Moves the player's circle down
        
        Args:
            width: display window width
            height: display window height

        Returns:
            None
        """
        if self.y + self.radius <= height:
            self.y += self.speed
            
    def move_left(self, width: int, height: int) -> None:
        """Moves the player's circle left
        
        Args:
            width: display window width
            height: display window height

        Returns:
            None
        """
        if self.x - self.radius >= 0:
            self.x -= self.speed
            
    def move_right(self, width: int, height: int) -> None:
        """Moves the player's circle right
        
        Args:
            width: display window width
            height: display window height

        Returns:
            None
        """
        if self.x + self.radius <= width:
            self.x += self.speed

    def collision(self, squares: list, balls: list) -> bool:
        """Detects if the player's circle has a collision with the list of objects given in the parameters

        Args:
            squares: A list of squares
            balls: A list of balls

        Returns:
            True if player's circle has a collision, False otherwise
        """
        for ball in balls:
            distance = math.sqrt((ball.x - self.x)**2 + (ball.y - self.y)**2)
            if distance < ball.radius + self.radius:
                return True
        for square in squares:
            square_radius = square.size/2
            distance = math.sqrt(((square.x + square_radius) - self.x)**2 + ((square.y + square_radius) - self.y)**2)
            if distance < square_radius + self.radius:
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
