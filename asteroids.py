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
            explosion = Explosion(self.position.x, self.position.y, self.radius)
           
    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        # Draw the asteroid on the screen
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius, width = 2)
    
class Debris(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, radius, size, lifetime):
        self.containers = (Debris.containers)
        if hasattr(self, "containers"):
            print(f"Debris: Using instance containers: {self.containers}")
            super().__init__(self.containers)
        else:
            print(f"Debris: No instance containers, using class containers: {Debris.containers}")
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity
        self.radius = radius
        self.size = size
        self.lifetime = lifetime
        self.base_color = [random.randint(200, 255) for _ in range (3)]
        self.color =  self.base_color.copy()
        print(f"Initialized debris at ({x}, {y}) with velocity {velocity}, size {size}, and lifetime {lifetime}")
    
    def update(self, dt):
        # Move debris
        self.position += self.velocity * dt
        self.lifetime -= dt
        # Face out debris
        fade_factor = max(0, self.lifetime / 1.0)
        self.color = [min(max(int(c * fade_factor), 0), 255) for c in self.base_color]
        # Check if the lifetime has expired and if so, remove debris
        if self.lifetime <= 0:
            self.kill()
        
    def draw(self, screen):
        # Draw the debris on the screen
         pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), int(self.size))
            

class Explosion(CircleShape):
    def __init__(self, x, y, radius):
        print(f"Creating Explosion at ({x}, {y})")
        super().__init__(x, y, radius)
        self.base_radius = radius
        self.explosion_radius = 5
        self.lifetime = 1.0
        self.time = 0.0
        self.color = [255, 255, 255]
        self.spawn_debris(x, y, radius)
    

    def spawn_debris(self, x, y, radius):
        num_debris = 10
        for _ in range(num_debris):
            angle_rad = random.uniform(0, 2 * 3.14159)
            angle_deg = angle_rad * (180 / 3.14159)
            speed = random.uniform(100, 250)
            velocity = pygame.Vector2(speed, 0).rotate(angle_deg)
            size = random.uniform(1.5, 3.5)
            lifetime = random.uniform(0.4, 1.2)
            # Create debris with a random position and velocity
            debris = Debris(x, y, velocity, radius, size, lifetime)
            
    
    def update(self, dt):
        super().update(dt)
        self.time += dt
        self.lifetime -= dt

        if self.time < 0.3:
            t = self.time / 0.3
            self.explosion_radius = 5 + t * (self.base_radius * 1.5 - 5)
        else:
            t = (self.time -0.3) / 0.7
            self.explosion_radius = self.base_radius * 1.5 * (1 - t)
        fade_factor = max(0, self.lifetime / 1)
        if self.time < 0.05: #White flash
            self.color = [255, 255, 255]
        elif self.time < 0.15:
            self.color = [255, 0, 0]
        elif self.time < 0.3: #OJ transition
            self.color = [255, 165, 0]
        else:
            self.color = [int(255 * fade_factor), int(255 * fade_factor), 0]

        if self.lifetime <= 0 or self.explosion_radius <= 0:
            self.kill()


    def draw(self, screen):
        # Draw the explosion on the screen
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.explosion_radius)
        
