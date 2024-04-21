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


def draw_background_border(surface):
    """
    Draw the border of the pool table.
    """
    # Draw the background
    surface.fill((0, 130, 0))

    # top border
    pygame.draw.rect(surface, config.Colors.BRONZE, (0, 0, 1400, 60))
    pygame.draw.rect(surface, config.Colors.BRONZE, (0, 740, 1400, 60))
    pygame.draw.rect(surface, config.Colors.BRONZE, (0, 0, 60, 800))
    pygame.draw.rect(surface, config.Colors.BRONZE, (1340, 0, 60, 800))

    holes_pos = [
        (70, 70),
        (1330, 70),
        (70, 730),
        (1330, 730),
        (700, 70),
        (700, 730)
    ]

    for hole in holes_pos:
        pygame.draw.circle(surface, config.Colors.SILVER, hole, 32)
        pygame.draw.circle(surface, config.Colors.BLACK, hole, 25)

    markers = [
        # top markers
        (280, 30),
        (280 * 2, 30),
        (280 * 3, 30),
        (280 * 4, 30),
        # bottom markers
        (280, 770),
        (280 * 2, 770),
        (280 * 3, 770),
        (280 * 4, 770),
        # left markers
        (30, 200),
        (30, 400),
        (30, 600),
        # right markers
        (1370, 200),
        (1370, 400),
        (1370, 600),
    ]
    for marker in markers:
        pygame.draw.circle(surface, config.Colors.SILVER, marker, 6)
