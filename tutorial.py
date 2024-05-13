import pygame
import sys
import config
from components import Button

pygame.init()

fonts = {
    'normal': pygame.font.Font('C:\\Windows\\Fonts\\arial.ttf', 24),
    'bold': pygame.font.Font('C:\\Windows\\Fonts\\arialbd.ttf', 26),
    'large': pygame.font.Font('C:\\Windows\\Fonts\\arial.ttf', 36)
}

tutorial_text = [
    "/bObjective: Billiards Master is a classic billiards game, in which the player's main goal is to get the cue ball to hit the remaining object balls to achieve the highest score.",
    "/bRules: Players will use the cue stick to hit the cue ball, push it to hit other balls on the table. The goal is to get the white ball to hit the object balls to put them in the pockets on the table.",
    "/bForm /bof /bplay: There can be many different forms of play such as 8-balls, 9-balls. Each form has its own rules and scoring methods."
]


def draw_background():
    """
    Vẽ nền cho màn hình hướng dẫn.
    """
    from utils import draw_main_menu_game_title, draw_background_border
    import config

    draw_background_border(config.gameDisplay)
    pygame.draw.rect(config.gameDisplay, config.Colors.FELT, (200, 175, 1000, 500), border_radius=15)
    draw_main_menu_game_title(config.gameDisplay, base_y=150, scale=0.5)


def draw_text_tutorial(text, color, surface, x, y):
    """
    Vẽ văn bản cho màn hình hướng dẫn.

    Tham số:
        text (str): Nội dung văn bản.
        color ((int, int, int)): Màu của văn bản dưới dạng bộ ba giá trị RGB.
        surface (pygame.Surface): Chỗ mà văn bản được vẽ.
        x (int): Tọa độ x của văn bản.
        y (int): Tọa độ y của văn bản.
    """
    global fonts
    words = text.split(' ')
    space = fonts['normal'].size(' ')[0]  # Khoảng cách giữa các từ
    for word in words:
        # Nếu từ bắt đầu bằng "/b", vẽ nó dưới dạng đậm.
        if word.startswith("/b"):
            word = word[2:]
            word_surface = fonts['bold'].render(word, 0, color)
        # Không thì vẽ nó dưới dạng bình thường.
        else:
            word_surface = fonts['normal'].render(word, 0, color)
        word_width, _ = word_surface.get_size()
        surface.blit(word_surface, (x, y))
        x += word_width + space


while True:
    draw_background()
    n_char_wrap = 90
    y = 250
    for text in tutorial_text:

        words = text.split(' ')
        lines = []

        while len(words) > 0:
            line = ''
            while len(words) > 0 and len(line + words[0]) <= n_char_wrap:
                line += words.pop(0) + ' '
            lines.append(line)

        for line in lines:
            draw_text_tutorial(line, config.Colors.WHITE, config.gameDisplay, 235, y)
            y += 50

        # Tăng khoảng cách giữa các đoạn văn bản
        y += 15

    # Vẽ nút "Back"
    back_btn = Button(
        text="Back",
        text_color=config.Colors.WHITE,
        font=config.Fonts.menu_small,
        pos=(100, 75),
        size=(150, 70),
        bg=pygame.transform.scale(
            pygame.image.load('images/menu_normal_btn_bg.png').convert_alpha(), 
            (150, 70)),
        target_display=config.gameDisplay
    )
    back_btn.draw()

    mx, my = pygame.mouse.get_pos()

    if back_btn.rect.collidepoint((mx, my)):
        if pygame.mouse.get_pressed()[0]:
            exec(open('main.py').read())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
