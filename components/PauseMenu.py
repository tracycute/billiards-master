import sys
import pygame

from components import Button
from utils import draw_main_menu_game_title
import config

def continue_game():
    config.game_is_paused = False

def draw_pause_menu():
    """Draw the pause menu and handle events."""
    btns_size = (400, 100)
    pause_text_size = (300, 80)
    play_btn_bg = pygame.image.load('images/menu_normal_btn_bg.png').convert_alpha()
    play_btn_bg = pygame.transform.scale(play_btn_bg, btns_size)
    exit_btn_bg = pygame.image.load('images/menu_exit_btn_bg.png').convert_alpha()
    exit_btn_bg = pygame.transform.scale(exit_btn_bg, pause_text_size)

    while config.game_is_paused:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for btn in btns.values():
                    if btn.rect.collidepoint((mx, my)):
                        btn.on_click()

            # Unpause game if 'p' is pressed
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    continue_game()
                    return

        btns = {
            'continue': Button(
                text="CONTINUE",
                text_color=config.WHITE,
                font=config.menuFont,
                pos=(500, 425),
                size=btns_size,
                bg=play_btn_bg,
                target_display=config.gameDisplay,
                on_click=lambda: continue_game(),
            ),
            'exit': Button(
                text="Exit",
                text_color=config.WHITE,
                font=config.menuFont,
                pos=(500, 535),
                size=btns_size,
                bg=play_btn_bg,
                target_display=config.gameDisplay,
                on_click=lambda: sys.exit(),
            ),
        }


        config.gameDisplay.fill((0, 130, 0))
        pygame.draw.rect(config.gameDisplay, config.FELT, (475, 360, 450, 300), border_radius=15)
        draw_main_menu_game_title(config.gameDisplay, 180, 0.8)
        
        for b in btns:
            btns[b].draw()
        
        pause_text = Button(
            text="PAUSED",
            text_color=config.WHITE,
            font=config.menuFont,
            pos=(550, 325),
            size=pause_text_size,
            bg=exit_btn_bg,
            target_display=config.gameDisplay,
        )
        pause_text.draw()

        pygame.display.update()
