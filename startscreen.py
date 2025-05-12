import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import random

def start_screen(screen):
    # Initialize fonts
    title_font = pygame.font.Font(None, 64)
    option_font = pygame.font.Font(None, 48)
    
    # Colors
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    
    # Create stars with positions and velocities
    stars = [{"pos": pygame.Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)),
              "vel": pygame.Vector2(random.uniform(-30, 30), random.uniform(-30, 30))}
             for _ in range(150)]
    
    # Alternative static starfield (uncomment to use)
    """
    starfield = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    for _ in range(150):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        pygame.draw.circle(starfield, white, (x, y), 2)
    """
    
    # Title
    title_text = title_font.render("Walkerer's Astr'oids", True, white)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, 100))
    
    # Options
    start_text = option_font.render("Start Game", True, white)
    start_rect = start_text.get_rect(center=(SCREEN_WIDTH / 2, 300))
    exit_text = option_font.render("Exit Game", True, white)
    exit_rect = exit_text.get_rect(center=(SCREEN_WIDTH / 2, 400))
    
    clock = pygame.time.Clock()
    while True:
        dt = clock.tick(60) / 1000  # Calculate delta time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_rect.collidepoint(event.pos):
                    return True
                if exit_rect.collidepoint(event.pos):
                    return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return True
                if event.key in (pygame.K_e, pygame.K_ESCAPE):
                    return False
        
        # Update star positions
        for star in stars:
            star["pos"] += star["vel"] * dt
            star["pos"].x %= SCREEN_WIDTH
            star["pos"].y %= SCREEN_HEIGHT
        
        # Mouse hover effect
        mouse_pos = pygame.mouse.get_pos()
        start_color = yellow if start_rect.collidepoint(mouse_pos) else white
        exit_color = yellow if exit_rect.collidepoint(mouse_pos) else white
        start_text = option_font.render("Start Game", True, start_color)
        exit_text = option_font.render("Exit Game", True, exit_color)
        
        # Draw
        screen.fill((0, 0, 0))  # Black background
        # For static starfield, uncomment: screen.blit(starfield, (0, 0))
        for star in stars:
            pygame.draw.circle(screen, white, (int(star["pos"].x), int(star["pos"].y)), 2)
        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(exit_text, exit_rect)
        pygame.display.flip()