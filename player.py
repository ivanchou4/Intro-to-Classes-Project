import pygame
import math


class Player:
    def __init__(self, x: int, y: int, radius: int, speed: int) -> None:
        """Constructs attributes related to the class, runs when an instance of this class has been made

        Args:
            x: The player's x position
            y: The player's y position
            radius: The player's circle radius
            speed: The player's speed during movements
        
        Returns:
            None
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.gun = Gun(10, 5)
    
    def move_up(self, width: int, height: int) -> None:
        """Attempts to moves the player's circle up on the screen, fails if the player is about to go off the screen
        
        Args:
            width: display window width
            height: display window height

        Returns:
            None
        """
        if self.y - self.radius >= 0:
            self.y -= self.speed
            
    def move_down(self, width: int, height: int) -> None:
        """Attempts to moves the player's circle down on the screen, fails if the player is about to go off the screen
        
        Args:
            width: display window width
            height: display window height

        Returns:
            None
        """
        if self.y + self.radius <= height - 100:
            self.y += self.speed
            
    def move_left(self, width: int, height: int) -> None:
        """Attempts to moves the player's circle left on the screen, fails if the player is about to go off the screen
        
        Args:
            width: display window width
            height: display window height

        Returns:
            None
        """
        if self.x - self.radius >= 0:
            self.x -= self.speed
            
    def move_right(self, width: int, height: int) -> None:
        """Attempts to moves the player's circle right on the screen, fails if the player is about to go off the screen
        
        Args:
            width: display window width
            height: display window height

        Returns:
            None
        """
        if self.x + self.radius <= width:
            self.x += self.speed

    def collision(self, balls: list) -> bool:
        """Detects if the player's circle has a collision with the list of balls given in the parameters

        Args:
            balls: A list of balls

        Returns:
            True if player's circle has a collision, False otherwise
        """
        for ball in balls:
            distance = math.sqrt((ball.x - self.x)**2 + (ball.y - self.y)**2)
            if distance < ball.radius + self.radius:
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


class Gun:
    def __init__(self, bullets: int, bullet_capacity: int) -> None:
        """Constructer
        
        Args:
            bullets: number of bullets that can be used
            bullet_capacity: Max amount of bullets that can be used at a time in the gun
        Returns:
            None
        """
        self._bullets = bullets
        self._magazine_capacity = bullet_capacity
        self._magazine_bullets = bullet_capacity
        
    def shoot(self, x: int, y: int, x_end: int, y_end: int) -> object:
        """Returns a Bullet class if there are builllets avaliable
        
        Args:
            x: Inital x position of bulllet
            y: Intial y poisition of bullet
            x_end: Where the bullet's x is going
            y_end: Where the bullet's y is going

        Returns:
            a Bullet object if there are bullets avaliable
        """
        if self._magazine_bullets > 0:
            self._magazine_bullets -= 1
            return Bullet(x, y, 2, x_end, y_end, 10)
        
    def reload(self) -> None:
        """Reloads the magazine if there are bullets avaliable
        
        Args:
            None
        
        Returns:
            None
        """
        if self._bullets >= 1:
            while self._bullets >= 1 and self._magazine_bullets != self._magazine_capacity:
                self._magazine_bullets += 1
                self._bullets -= 1

    def set_bullets(self, bullets: int):
        if bullets >= 0:
            self._bullets = bullets
        else:
            raise ValueError("You cannot have a negative amount of bullets.")

    def set_magazine_capacity(self, new_capacity: int) -> None:
        """Sets a new magazine capacity
        
        Args:
            new_capacity = A non-negative number
        
        Returns:
            None
        """
        if new_capacity >= 0:
            self._magazine_capacity = new_capacity
        else:
            raise ValueError("You cannot have a magazine capacity that is less than zero.")

    def get_bullets(self) -> int:
        return self._bullets

    def get_magazine_bullets(self) -> int:
        return self._magazine_bullets

    def get_magazine_capacity(self) -> int:
        return self._magazine_capacity

class Bullet:
    def __init__(self, x: int, y: int, radius: int, x_end: int, y_end: int, speed: int) -> None:
        """Constructs attributes related to the class, runs when an instance of this class has been made

        Args:
            x: The bullet's x position
            y: The bullet's y position
            radius: The bullet's circle radius
            x_end: The end destination of the bullet's x value
            y_end: The end destination of the bullet's y value
            speed: The speed of the bullet

        Returns:
            None
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.unit_vector = ((x_end - x)/math.sqrt((x_end - x)**2 + (y_end - y)**2), (y_end - y)/math.sqrt((x_end - x)**2 + (y_end - y)**2))
        self.speed_multiplier = speed

    def move(self) -> None:
        """Updates the bullet's x and y positions

        Args:
            None

        Returns:
            None
        """
        self.x += self.speed_multiplier * self.unit_vector[0]
        self.y += self.speed_multiplier * self.unit_vector[1]

    def on_hit(self, circle_x: int, circle_y: int, circle_radius: int) -> bool:
        """Detects if the bullet's circle has hit the circle hitbox given in the parameters

        Args:
            circle_x = Circle hitbox's x position
            circle_y = Circle hitbox's y position
            circle_radius = Circle hitbox's radius

        Returns:
            True if the bullet hits the hitbox. False otherwise
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
