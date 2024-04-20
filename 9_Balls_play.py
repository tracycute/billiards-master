import pygame
import config
pygame.init()


def draw_background():
    global config
    config.gameDisplay.fill(config.BROWN)
    pygame.draw.rect(config.gameDisplay, config.FELT, (200, 150, 1000, 500))
    for wall in config.walls: 
        pygame.draw.rect(config.gameDisplay, config.BRONZE, wall)
    for hole in config.holes: 
        pygame.draw.circle(config.gameDisplay, config.BLACK, hole, 22)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    draw_background()
    pygame.display.update()
    pygame.time.Clock().tick(60)