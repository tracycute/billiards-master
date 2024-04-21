import sys
import pygame

from components import Button
from utils import draw_main_menu_game_title
from components import Player
import config

def restart_game():
    config.init_game_states()

    print('states are reset')
    config.game_is_paused = False
    config.prevent_shoot = True

    
def draw(winner: Player):
    """Draw the pause menu and handle events."""
    btns_size = (400, 100)
    play_btn_bg = pygame.image.load('images/menu_normal_btn_bg.png').convert_alpha()
    play_btn_bg = pygame.transform.scale(play_btn_bg, btns_size)

    btns = {
        'continue': Button(
            text="PLAY AGAIN",
            text_color=config.Colors.WHITE,
            font=config.Fonts.menu,
            pos=(500, 435),
            size=btns_size,
            bg=play_btn_bg,
            target_display=config.gameDisplay,
            on_click=restart_game,
        ),
        'exit': Button(
            text="Exit",
            text_color=config.Colors.WHITE,
            font=config.Fonts.menu,
            pos=(500, 545),
            size=btns_size,
            bg=play_btn_bg,
            target_display=config.gameDisplay,
            on_click=lambda: sys.exit(),
        ),
    }

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

        config.gameDisplay.fill((0, 130, 0))

        pygame.draw.rect(config.gameDisplay, config.Colors.FELT, (470, 340, 460, 320), border_radius=15)
        draw_main_menu_game_title(config.gameDisplay, 180, 0.8)

        # Draw the winner
        winner_text = config.Fonts.menu.render(f'PLAYER {winner.number} WINS', True, config.Colors.YELLOW)
        config.gameDisplay.blit(winner_text, (500, 350))

        for b in btns:
            btns[b].draw()

        pygame.display.update()
