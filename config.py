import pygame

pygame.init()

# fonts
mainFont = pygame.font.SysFont("freesansbold.ttf", 30)
menuFont_path = '.\\fonts\\lemon-regular.TTF'
menuFont = pygame.font.Font(menuFont_path, 50)

# display
gameDisplay = pygame.display.set_mode((1400, 800))
pygame.display.set_caption('Billiard Master')
clock = pygame.time.Clock()

walls = (
    pygame.Rect(150, 100, 1100, 50),
    pygame.Rect(150, 650, 1100, 50),
    pygame.Rect(1200, 100, 50, 600),
    pygame.Rect(150, 100, 50, 600)
)

holes = (
    (210, 160),
    (700, 150),
    (1190, 160),
    (210, 640),
    (700, 650),
    (1190, 640)
)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FELT = (4, 105, 36)
OAK = (79, 36, 18)
RED = (255, 0, 0)
BRONZE = (131, 79,  22)
BROWN = (43, 3, 18)
P1 = (255, 5, 0)
P2 = (255, 211, 0)