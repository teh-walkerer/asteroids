from circleshape import CircleShape
from constants import *
from shots import Shot  # Import the Shot class from the appropriate module
import pygame


shoot_timer = 0.0
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        self.tripleshot_active = False
        self.tripleshot_timer = 0

        
        
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            # turn left
        if keys[pygame.K_d]:
            self.rotate(dt)
            # turn right
        if keys[pygame.K_w]:
            self.move(dt)
            # move forward
        if keys[pygame.K_s]:
            self.move(-dt)
            # move backward
        if keys[pygame.K_SPACE]:
            self.shoot()
            # shoot
        if self.shoot_timer > 0:
            self.shoot_timer -= dt    
        
        if self.tripleshot_active:
            self.tripleshot_timer -= dt
            if self.tripleshot_timer <= 0:
                self.tripleshot_active = False
                self.tripleshot_timer = 0
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
            # move forward
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    
    def shoot(self):
        if self.shoot_timer > 0:
            return

        if not self.tripleshot_active:
            shot = Shot(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
        else:
            shot = Shot(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shot2 = Shot(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
            shot2.velocity = pygame.Vector2(0, 1).rotate(self.rotation + 10) * PLAYER_SHOOT_SPEED
            shot3 = Shot(self.position.x, self.position.y, PLAYER_SHOT_RADIUS)
            shot3.velocity = pygame.Vector2(0, 1).rotate(self.rotation - 10) * PLAYER_SHOOT_SPEED
            

        self.shoot_timer = self.shoot_cooldown

        return shot
    
