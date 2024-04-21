import pygame
import config

def draw_main_menu_game_title(surface, base_y=100, scale=1.0):
    """
    Draw the game title on the main menu.

    Parameters
    ----------
    surface: pygame.Surface, required
        The surface to draw the title on.

    base_y: int, optional, default 100
        The y-coordinate of the base of the title.

    scale: float, optional, default 1.0
        The scale of the title.
    """
    title_font_1 = pygame.font.Font(config.Fonts.path_menu, int(100 * scale))
    title_font_2 = pygame.font.Font(config.Fonts.path_menu, int(120 * scale))

    color = (255, 255, 255)

    textobj = title_font_1.render("BILLIARD", 1, color)
    textrect = textobj.get_rect()
    textrect.center = (700, base_y)
    surface.blit(textobj, textrect)

    textobj = title_font_2.render("MASTER", 1, color)
    textrect = textobj.get_rect()
    textrect.center = (700, base_y + 100*scale)
    surface.blit(textobj, textrect)

