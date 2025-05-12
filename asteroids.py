import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.x = x
        self.y = y
        self.color = (255, 255, 255)  # White color for the asteroid
        self.velocity = pygame.Vector2(0, 0)  # Initial velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            rotation_vector1 = self.velocity.rotate(random_angle)
            rotation_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = rotation_vector1
            new_asteroid2.velocity = rotation_vector2
    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        # Draw the asteroid on the screen
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius, width = 2)