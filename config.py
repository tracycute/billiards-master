import pygame
from components import Player, Ball

pygame.init()


class Fonts:
    """Font chữ được sử dụng trong trò chơi."""
    path_menu = ".\\fonts\\lemon-regular.TTF"
    path_basic = "freesansbold.ttf"

    basic = pygame.font.Font(path_basic, 30)

    menu = pygame.font.Font(path_menu, 50)
    menu_small = pygame.font.Font(path_menu, 30)

# Âm thanh
hit_sound = pygame.mixer.Sound('sounds/hit.wav')
sunk_sound = pygame.mixer.Sound('sounds/sunk.ogg')
strike_sound = pygame.mixer.Sound('sounds/strike.wav')

# Màn hình
gameDisplay = pygame.display.set_mode((1400, 800))
pygame.display.set_caption('Billiards Master')
clock = pygame.time.Clock()


class Colors:
    """Màu sắc được sử dụng trong trò chơi."""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FELT = (4, 105, 36)
    OAK = (79, 36, 18)
    RED = (255, 0, 0)
    BRONZE = (131, 79, 22)
    BROWN = (43, 3, 18)
    YELLOW = (255, 211, 0)
    SILVER = (170, 170, 170)
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

# Khởi tạo thông tin về người chơi
player_1, player_2 = Player(1, ''), Player(2, '')
player_turn = player_1

# Gậy đánh
pool_cue_original = pygame.image.load('images/cue.png').convert_alpha()
pool_cue_rotated = pygame.transform.rotate(pool_cue_original, 0)
pool_cue_coords = (0, 0)

# Chuột
mouse_hold_coords = (0, 0)
mouse_held = False

strike_distance = 0
draw_guide = True
in_play = False
# Kiểm tra xem lượt đánh có phải là lượt đánh đầu tiên không
initial_break = True

# Một số biến khác
cue_ball_in_hand = False
turn_change = True
first_ball_collided_with = None
game_is_paused = False
prevent_shoot = False

# Bi cơ
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
    """
    Khởi tạo lại trạng thái của trò chơi.

    Reset các biến và đối tượng liên quan đến trạng thái của trò chơi về trạng thái ban đầu.
    """
    global player_1, player_2, player_turn, \
        pool_cue_original, pool_cue_rotated, pool_cue_coords,\
        mouse_hold_coords, mouse_held, strike_distance, draw_guide, in_play, initial_break,\
        cue_ball_in_hand, turn_change, first_ball_collided_with, winner,\
        cue_ball, cue_direction, balls, balls_9, recent_potted_balls, potted_balls, \
        recent_balls_9, check_collision_recent_ball_9, \
        game_is_paused

    # Reset thông tin về người chơi
    player_1.reset_state()
    player_2.reset_state()
    player_turn = player_1

    # Reset thông tin về gậy đánh và chuột
    pool_cue_original = pygame.image.load('images/cue.png').convert_alpha()
    pool_cue_rotated = pygame.transform.rotate(pool_cue_original, 0)

    pool_cue_coords = (0, 0)

    mouse_hold_coords = (0, 0)
    mouse_held = False

    # Reset thông tin về cú đánh và hướng đánh
    strike_distance = 0
    draw_guide = True

    # Reset trạng thái trò chơi
    in_play = False
    initial_break = True

    # Reset thông tin về bi cơ và lượt đánh
    cue_ball_in_hand = False
    turn_change = True
    first_ball_collided_with = None

    # Reset thông tin về bi và lỗ
    cue_ball.x, cue_ball.y = 450, 400

    for i, ball in enumerate(balls):
        ball.reset_state()
        ball.x, ball.y = balls_initial_pos[i]

    for i, ball in enumerate(balls_9):
        ball.reset_state()
        ball.x, ball.y = balls_9_initial_pos[i]


    # Reset thông tin về các bi đã rơi
    recent_potted_balls = []
    potted_balls = []
    recent_balls_9 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    check_collision_recent_ball_9 = False


init_game_states()
