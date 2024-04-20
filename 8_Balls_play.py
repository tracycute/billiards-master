import pygame
import config
from components.PoolTable import draw_background
pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # we don't handle any mouse events if the game is in play
        if config.in_play:
            continue

        if event.type == pygame.MOUSEBUTTONDOWN:
            config.mouse_hold_coords = event.pos
            config.mouse_held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            config.mouse_held = False

            if config.strike_distance > 16:
                config.draw_guide = False
                config.in_play = True
        elif event.type == pygame.MOUSEMOTION and not config.mouse_held:
            config.draw_guide = True
            config.mouse_hold_coords = event.pos
        else:
            pass



    draw_background()

    for ball in config.balls:
        # if the ball is potted, we don't draw it
        if ball.potted:
            continue

        config.gameDisplay.blit(ball.sprite, (ball.x - 18, ball.y - 18))

    if not config.in_play:
        if config.draw_guide:
            pygame.draw.line(
                surface=config.gameDisplay, 
                color=config.RED, 
                start_pos=(config.cue_ball.x, config.cue_ball.y), 
                end_pos=config.mouse_hold_coords,
                width=2
            )


    pygame.display.update()
    pygame.time.Clock().tick(60)