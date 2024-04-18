import pygame
from config import menuFont, menuFont_path

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
    titleFont_1 = pygame.font.Font(menuFont_path, int(100 * scale))
    titleFont_2 = pygame.font.Font(menuFont_path, int(120 * scale))

    color = (255, 255, 255)

    textobj = titleFont_1.render("BILLIARD", 1, color)
    textrect = textobj.get_rect()
    textrect.center = (700, base_y)
    surface.blit(textobj, textrect)

    textobj = titleFont_2.render("MASTER", 1, color)
    textrect = textobj.get_rect()
    textrect.center = (700, base_y + 100*scale)
    surface.blit(textobj, textrect)

