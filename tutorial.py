import pygame
import sys
import config
from utils import draw_main_menu_game_title
from components import Button

pygame.init()

fonts = {
    'normal': pygame.font.Font('C:\\Windows\\Fonts\\arial.ttf', 24),
    'bold': pygame.font.Font('C:\\Windows\\Fonts\\arialbd.ttf', 26),
    'large': pygame.font.Font('C:\\Windows\\Fonts\\arial.ttf', 36)
}

tutorial_text = [
    "/bObjective: Billiard Master is a classic billiards game, in which the player's main goal is to get the cue ball to hit the remaining object balls to achieve the highest score.",
    "/bRules: Players will use the cue stick to hit the cue ball, push it to hit other balls on the table. The goal is to get the white ball to hit the object balls to put them in the pockets on the table.",
    "/bForm /bof /bplay: There can be many different forms of play such as 8-balls, 9-balls. Each form has its own rules and scoring methods."
]


def draw_background():
    global config
    config.gameDisplay.fill((0, 130, 0))
    pygame.draw.rect(config.gameDisplay, config.Colors.FELT, (200, 150, 1000, 500), border_radius=15)
    draw_main_menu_game_title(config.gameDisplay, scale=0.5)


def draw_text_tutorial(text, color, surface, x, y):
    global fonts
    words = text.split(' ')
    space = fonts['normal'].size(' ')[0]  # The width of a space.
    for word in words:
        # If the word starts with "/b", render it in bold.
        if word.startswith("/b"):
            word = word[2:]
            word_surface = fonts['bold'].render(word, 0, color)
        # Otherwise, render it normally.
        else:
            word_surface = fonts['normal'].render(word, 0, color)
        word_width, _ = word_surface.get_size()
        surface.blit(word_surface, (x, y))
        x += word_width + space


while True:
    draw_background()
    n_char_wrap = 90
    y = 200
    for text in tutorial_text:

        words = text.split(' ')
        lines = []

        while len(words) > 0:
            line = ''
            while len(words) > 0 and len(line + words[0]) <= n_char_wrap:
                line += words.pop(0) + ' '
            lines.append(line)

        for line in lines:
            draw_text_tutorial(line, config.Colors.WHITE, config.gameDisplay, 230, y)
            y += 50

        # extra space between paragraphs
        y += 15

    # Draw "back" button
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
