import pygame


class Button:
    def __init__(self,
                 text: str,
                 text_color: tuple,
                 font: pygame.font.Font,
                 pos: tuple,
                 size: tuple,
                 bg: pygame.surface.Surface,
                 target_display: pygame.surface.Surface,
                 on_click=None,
                 ):
        self.text = text
        self.text_color = text_color
        self.font = font
        self.pos = pos
        self.size = size
        self.bg = bg
        self.target_display = target_display
        self.rect = pygame.Rect(self.pos, self.size)
        self.on_click = on_click

    def draw(self):
        self.target_display.blit(self.bg, self.pos)

        text = self.font.render(self.text, 1, self.text_color)
        text_rect = text.get_rect()

        x = self.pos[0] + (self.size[0] // 2)
        y = self.pos[1] + (self.size[1] // 2)
        text_rect.center = (x, y)

        self.target_display.blit(text, text_rect)
