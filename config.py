import pygame
from components import Player, Ball

pygame.init()


class Fonts:
    """Font constants."""
    path_menu = ".\\fonts\\lemon-regular.TTF"
    path_basic = "freesansbold.ttf"

    basic = pygame.font.Font(path_basic, 30)

    menu = pygame.font.Font(path_menu, 50)
    menu_small = pygame.font.Font(path_menu, 30)


# display
gameDisplay = pygame.display.set_mode((1400, 800))
pygame.display.set_caption('Billiard Master')
clock = pygame.time.Clock()


class Colors:
    """Color constants."""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FELT = (4, 105, 36)
    OAK = (79, 36, 18)
    RED = (255, 0, 0)
    BRONZE = (131, 79, 22)
    BROWN = (43, 3, 18)
    YELLOW = (255, 211, 0)
    P1 = (255, 5, 0)
    P2 = (255, 211, 0)


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

# Init players
player_1, player_2 = Player(1, ''), Player(2, '')
player_turn = player_1

# pool cue
pool_cue_original = pygame.image.load('images/cue.png').convert_alpha()
pool_cue_rotated = pygame.transform.rotate(pool_cue_original, 0)
pool_cue_coords = (0, 0)

# mouse
mouse_hold_coords = (0, 0)
mouse_held = False

strike_distance = 0
draw_guide = True
in_play = False
# check stripes and solids was assigned
initial_break = True

# some setting
cue_ball_in_hand = False
turn_change = True
first_ball_collided_with = None
game_is_paused = False
prevent_shoot = False

# Balls
cue_ball = Ball('', 450, 400, 'images/ball0.png')
cue_direction = 0

balls_initial_pos = [
    (450, 400),
    (915+6, 400),
    (915+36*2, 400+36),
    (915+36*4-6, 400+36),
    (915+36*4-6, 400-36*2),
    (915+36+3, 400-18),
    (915+36*3-3, 400+18*3),
    (915+36*3-3, 400-18*3),
    (915+36*2, 400),
    (915+36*2, 400-36),
    (915+36*3-3, 400+18),
    (915+36*3-3, 400-18),
    (915+36*4-6, 400+36*2),
    (915+36*4-6, 400-36),
    (915+36+3, 400+18),
    (915+36*4-6, 400),
]
balls = [
    cue_ball,
    Ball('solids', 915+6, 400, 'images/ball1.png'),
    Ball('solids', 915+36*2, 400+36, 'images/ball2.png'),  # 950 - 36, 400
    Ball('solids', 915+36*4-6, 400+36, 'images/ball3.png'),
    Ball('solids', 915+36*4-6, 400-36*2, 'images/ball4.png'),
    Ball('solids', 915+36+3, 400-18, 'images/ball5.png'),
    Ball('solids', 915+36*3-3, 400+18*3, 'images/ball6.png'),
    Ball('solids', 915+36*3-3, 400-18*3, 'images/ball7.png'),
    Ball('eight', 915+36*2, 400, 'images/ball8.png'),
    Ball('stripes', 915+36*2, 400-36, 'images/ball9.png'),
    Ball('stripes', 915+36*3-3, 400+18, 'images/ball10.png'),
    Ball('stripes', 915+36*3-3, 400-18, 'images/ball11.png'),
    Ball('stripes', 915+36*4-6, 400+36*2, 'images/ball12.png'),
    Ball('stripes', 915+36*4-6, 400-36, 'images/ball13.png'),
    Ball('stripes', 915+36+3, 400+18, 'images/ball14.png'),
    Ball('stripes', 915+36*4-6, 400, 'images/ball15.png')
]

balls_9_initial_pos = [
    (450, 400),
    (915+6, 400),
    (915+36+3, 400-18),
    (915+36+3, 400+18),
    (915+36*2, 400+36),
    (915+36*2, 400-36),
    (915+36*3-3, 400-18),
    (915+36*3-3, 400+18),
    (915+36*4-6, 400),
    (915+36*2, 400)
]
balls_9 = [
    cue_ball,
    Ball("one", 915+6, 400, 'images/ball1.png'),
    Ball("two", 915+36+3, 400-18, 'images/ball2.png'),  # 950 - 36, 400
    Ball("three", 915+36+3, 400+18, 'images/ball3.png'),
    Ball("four", 915+36*2, 400+36, 'images/ball4.png'),
    Ball("five", 915+36*2, 400-36, 'images/ball5.png'),
    Ball("six", 915+36*3-3, 400-18, 'images/ball6.png'),
    Ball("seven", 915+36*3-3, 400+18, 'images/ball7.png'),
    Ball("eight", 915+36*4-6, 400, 'images/ball8.png'),
    Ball("nine", 915+36*2, 400, 'images/ball9.png')
]

recent_potted_balls = []
potted_balls = []
recent_balls_9 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

check_collision_recent_ball_9 = False


def init_game_states():
    global player_1, player_2, player_turn, \
        pool_cue_original, pool_cue_rotated, pool_cue_coords,\
        mouse_hold_coords, mouse_held, strike_distance, draw_guide, in_play, initial_break,\
        cue_ball_in_hand, turn_change, first_ball_collided_with, winner,\
        cue_ball, cue_direction, balls, balls_9, recent_potted_balls, potted_balls, \
        recent_balls_9, check_collision_recent_ball_9, \
        game_is_paused

    player_1.reset_state()
    player_2.reset_state()
    player_turn = player_1

    pool_cue_original = pygame.image.load('images/cue.png').convert_alpha()
    pool_cue_rotated = pygame.transform.rotate(pool_cue_original, 0)

    pool_cue_coords = (0, 0)

    mouse_hold_coords = (0, 0)
    mouse_held = False

    strike_distance = 0
    draw_guide = True

    in_play = False
    initial_break = True

    cue_ball_in_hand = False
    turn_change = True
    first_ball_collided_with = None

    # reset balls position
    cue_ball.x, cue_ball.y = 450, 400

    for i, ball in enumerate(balls):
        ball.reset_state()
        ball.x, ball.y = balls_initial_pos[i]

    for i, ball in enumerate(balls_9):
        ball.reset_state()
        ball.x, ball.y = balls_9_initial_pos[i]


    recent_potted_balls = []
    potted_balls = []
    recent_balls_9 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    check_collision_recent_ball_9 = False


init_game_states()
