import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroids import Asteroid, Explosion, Debris
from shots import Shot
from powerups import TripleShotPowerUp
from startscreen import start_screen
import sys
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

     # Show start screen
    if not start_screen(screen):
        pygame.quit()
        sys.exit()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    debris_group = pygame.sprite.Group()
    explosion = pygame.sprite.Group()
    

    
    Asteroid.containers = (updatable, drawables, asteroids)
    Debris.containers = (updatable, drawables, debris_group)
    Explosion.containers = (updatable, drawables, explosion)
    Shot.containers = (updatable, drawables, shots)
    TripleShotPowerUp.containers = (updatable, drawables, powerups)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawables)
    print(f"Debris.containers: {Debris.containers}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    score = 0
    dt = 0
    font = pygame.font.Font(None, 36)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        for powerup in powerups:
            if player.collision(powerup):
                print("Power-up collected!")
                # Handle power-up collection (e.g., activate power-up, increase score, etc.)
                # For now, just print a message
                # You can also remove the power-up here if needed
                powerup.kill()
                player.tripleshot_active = True
                player.tripleshot_timer = TRIPLE_SHOT_DURATION
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                # Handle collision (e.g., end game, reduce health, etc.)
                # For now, just print a message
                # You can also remove the asteroid or player here if needed
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    
                    # Handle collision (e.g., destroy asteroid, score points, etc.)
                    # For now, just print a message
                    # You can also remove the asteroid or shot here if needed
                    score += 10

                    asteroid.split()

                    shot.kill()
                    

                

                    if random.random() < POWERUP_DROP_RATE:
                        powerup = TripleShotPowerUp(asteroid.position.x, asteroid.position.y)
                        powerup.velocity = asteroid.velocity
                    
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()