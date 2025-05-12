import pygame
from circleshape import CircleShape


class TripleShotPowerUp(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 10)  # Assuming a radius of 10 for the power-up
        self.color = (255, 0, 0)  # Red color for the power-up
        self.active = True  # Indicates if the power-up is active

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)