import pygame
import math


class Square:

    def __init__(self, x:int, y:int, speed_x: int, speed_y: int): 
        """
        Takes all the attributes of the square. (x,y) position, size, and (x,y) velocity
        Args:
        x: the x position of the square
        y: the y position of the square
        size: the length of the square's sides
        speed_y: the speed of the square in the y direction
        speed_x: the speed of the square in the x direction
        Returns:
        nothing
        
        """
        self.x = x
        self.y = y
        self.size = 20
        self.speed_x = speed_x
        self.speed_y = speed_y
    def move(self) -> None:
        """
        updates the position of the squre for every tick to get the sq uare to move
        Args:
        nothing
        """
        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.x < 0 or self.x > 640:
            self.speed_x *= -1
        if self.y <0 or self.y > 480:
            self.speed_y *= -1
        
        
    def draw(self, surface) -> None:
        """
        Draws the square onto the screen
        Args: 
        None
        Returns: 
        None
        """
        pygame.draw.rect(surface, (0, 0, 200), (self.x, self.y, self.size, self.size))
