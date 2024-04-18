import pygame
import sys
from config import gameDisplay, menuFont, WHITE
from utils import draw_main_menu_game_title
from components import Button

pygame.init()
click = False
btns_size = (300, 100)

play_btn_bg = pygame.image.load('images/menu_normal_btn_bg.png').convert_alpha()
play_btn_bg = pygame.transform.scale(play_btn_bg, btns_size)
exit_btn_bg = pygame.image.load('images/menu_exit_btn_bg.png').convert_alpha()
exit_btn_bg = pygame.transform.scale(exit_btn_bg, btns_size)


btns = {
    '8 Balls': Button(
        text="8 Balls",
        text_color=WHITE,
        font=menuFont,
        pos=(550, 290),
        size=btns_size,
        bg=play_btn_bg,
        target_display=gameDisplay,
        on_click=lambda: exec(open('8_Balls_play.py').read()),
    ),
    '9 Balls': Button(
        text="9 Balls",
        text_color=WHITE,
        font=menuFont,
        pos=(550, 415),
        size=btns_size,
        bg=play_btn_bg,
        target_display=gameDisplay,
        on_click=lambda: exec(open('9_Balls_play.py').read()),
    ),
    'Tutorial': Button(
        text="Tutorial",
        text_color=WHITE,
        font=menuFont,
        pos=(550, 540),
        size=btns_size,
        bg=play_btn_bg,
        target_display=gameDisplay,
        on_click=lambda: exec(open('tutorial.py').read()),
    ),
    'Quit': Button(
        text="Quit",
        text_color=WHITE,
        font=menuFont,
        pos=(550, 665),
        size=btns_size,
        bg=exit_btn_bg,
        target_display=gameDisplay,
        on_click=lambda: sys.exit(),
    ),
}


def menu():
    global click
    while True:
        gameDisplay.fill((0, 130, 0))

        # Draw game title on screen
        draw_main_menu_game_title(gameDisplay)

        # Draw buttons on screen
        for btn in btns.values():
            btn.draw()

        # Check if any button is clicked
        mx, my = pygame.mouse.get_pos()
        for btn in btns.values():
            if btn.rect.collidepoint((mx, my)):
                if click:
                    btn.on_click()

        click = False

        # Check if user wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


if __name__ == '__main__':
    menu()
