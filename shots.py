import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.x = x
        self.y = y
        self.color = (255, 255, 255)  # White color for the shot
        self.velocity = pygame.Vector2(0, 0)  # Initial velocity

    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        # Draw the shot on the screen
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)

