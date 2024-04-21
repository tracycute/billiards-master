import pygame
import config

def draw_background():
    """Draws the background of the pool table."""
    global config
    config.gameDisplay.fill(config.Colors.BROWN)
    pygame.draw.rect(config.gameDisplay, config.Colors.FELT, (200, 150, 1000, 500))
    for wall in config.walls: 
        pygame.draw.rect(config.gameDisplay, config.Colors.BRONZE, wall)
    for hole in config.holes: 
        pygame.draw.circle(config.gameDisplay, config.Colors.BLACK, hole, 22)
    
    # Draw players info
    p1_color = config.player_1.color
    p2_color = config.player_2.color
    config.gameDisplay.blit(config.Fonts.basic.render('PLAYER 1', 1, config.Colors.P1), (20, 10))
    config.gameDisplay.blit(config.Fonts.basic.render(p1_color.upper(), 1, config.Colors.P1), (20, 50))
    config.gameDisplay.blit(config.Fonts.basic.render('PLAYER 2', 1, config.Colors.P2), (1240, 10))
    config.gameDisplay.blit(config.Fonts.basic.render(p2_color.upper(), 1, config.Colors.P2), (1240, 50))
