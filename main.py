import pygame
import sys
import config
from components import Button

pygame.init()
click = False
btns_size = (300, 80)

play_btn_bg = pygame.image.load('images/menu_normal_btn_bg.png').convert_alpha()
play_btn_bg = pygame.transform.scale(play_btn_bg, btns_size)
exit_btn_bg = pygame.image.load('images/menu_exit_btn_bg.png').convert_alpha()
exit_btn_bg = pygame.transform.scale(exit_btn_bg, btns_size)


btns = {
    '8 Balls': Button(
        text="8 Balls",
        text_color=config.Colors.WHITE,
        font=config.Fonts.menu,
        pos=(550, 300),
        size=btns_size,
        bg=play_btn_bg,
        target_display=config.gameDisplay,
        on_click=lambda: exec(open('8_Balls_play.py').read()),
    ),
    '9 Balls': Button(
        text="9 Balls",
        text_color=config.Colors.WHITE,
        font=config.Fonts.menu,
        pos=(550, 395),
        size=btns_size,
        bg=play_btn_bg,
        target_display=config.gameDisplay,
        on_click=lambda: exec(open('9_Balls_play.py').read()),
    ),
    'Tutorial': Button(
        text="Tutorial",
        text_color=config.Colors.WHITE,
        font=config.Fonts.menu,
        pos=(550, 490),
        size=btns_size,
        bg=play_btn_bg,
        target_display=config.gameDisplay,
        on_click=lambda: exec(open('tutorial.py').read()),
    ),
    'Exit': Button(
        text="Exit",
        text_color=config.Colors.WHITE,
        font=config.Fonts.menu,
        pos=(550, 585),
        size=btns_size,
        bg=exit_btn_bg,
        target_display=config.gameDisplay,
        on_click=lambda: sys.exit(),
    ),
}


def menu():
    """Màn hình chính của game

    Hiển thị các nút chức năng chính của game.
    """
    from utils import draw_main_menu_game_title, draw_background_border
    import config
    global click
    while True:

        config.gameDisplay.fill((0, 130, 0))

        draw_background_border(config.gameDisplay)

        # Vẽ tiêu đề của game
        draw_main_menu_game_title(config.gameDisplay, base_y=150, scale=0.8)

        # Vẽ các nút chức năng
        for btn in btns.values():
            btn.draw()

        # Kiểm tra xem người chơi đã click vào nút nào chưa
        mx, my = pygame.mouse.get_pos()
        for btn in btns.values():
            if btn.rect.collidepoint((mx, my)):
                if click:
                    btn.on_click()

        click = False

        # Kiểm tra sự kiện thoát game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


menu()
