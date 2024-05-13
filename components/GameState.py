import pygame
import sys
from config import *
from .Collisions import *
from .PoolTable import draw_background
from .Player import *
def player_turn_switch(turn):
    """
    Chuyển đổi lượt chơi giữa hai người chơi.

    Tham số:
    - turn: Đối tượng của người chơi hiện tại.

    Trả về:
    Đối tượng của người chơi tiếp theo.
    """
    if turn.number == 1:
        return player_2
    elif turn.number == 2:
        return player_1

def balls_stopped():
    """
    Kiểm tra xem tất cả các quả bi đã dừng lại hay chưa.

    Trả về:
    True nếu tất cả các quả bi đã dừng lại, False nếu còn ít nhất một quả bi đang di chuyển.
    """
    for ball in balls: 
        if ball.speed > 0 and not ball.potted:
            return False
    return True

def balls_stopped_9():
    """
    Kiểm tra xem tất cả các quả bi  đã dừng lại hay chưa trong 9 ball.
    """
    for ball in balls_9:
        if ball.speed > 0 and not ball.potted:
            return False
    return True

def ball_potted(x, y):
    """
    Kiểm tra xem quả bi có bị rơi vào lỗ hay không.

    Tham số:
    - x: Tọa độ x của quả bi.
    - y: Tọa độ y của quả bi.

    Trả về:
    True nếu quả bi bị rơi vào lỗ, False nếu không.
    """
    for hole in holes:
        if distance_between_points(x, y, hole[0], hole[1]) < 30:
            return True
    return False

def ball_in_hand():
    """
    Hàm này được sử dụng khi một quả bi bị rơi vào lỗ và cần được đặt lại ở vị trí mới trên bàn.
    """
    ball_dropped = False
    button_down = False
    while not ball_dropped:
        draw_background()
        draw_potted_balls()
        for ball in balls:
            if not ball.potted: gameDisplay.blit(ball.sprite, (ball.x - 18, ball.y - 18))
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEMOTION:
                mouseX, mouseY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                if 217 < mouseX < 1184 and 160 < mouseY < 634:
                    if check_collision_with_other_ball(mouseX, mouseY, cue_ball) is None:
                        cue_ball.x, cue_ball.y = mouseX, mouseY
            if e.type == pygame.MOUSEBUTTONDOWN:
                button_down = True
            if e.type == pygame.MOUSEBUTTONUP and button_down:
                ball_dropped = True

def ball_in_hand_9():
    """
    Hàm này được sử dụng khi quả bi cái bị rơi vào lỗ và cần được đặt lại ở vị trí mới trên bàn trong game 9 ball.
    """
    ball_dropped = False
    button_down = False
    while not ball_dropped:
        draw_background()
        draw_potted_balls()
        for ball in balls_9:
            if not ball.potted: gameDisplay.blit(ball.sprite, (ball.x - 18, ball.y - 18))
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEMOTION:
                mouseX, mouseY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                if 217 < mouseX < 1184 and 160 < mouseY < 634:
                    if check_collision_with_other_ball(mouseX, mouseY, cue_ball) is None:
                        cue_ball.x, cue_ball.y = mouseX, mouseY
            if e.type == pygame.MOUSEBUTTONDOWN:
                button_down = True
            if e.type == pygame.MOUSEBUTTONUP and button_down:
                ball_dropped = True

def number_of_balls_potted(c):
    """
    Đếm số lượng quả bi cụ thể đã bị rơi vào lỗ.

    Tham số:
    - c: Màu của quả bi cần đếm.

    Trả về:
    Số lượng quả bi có màu cụ thể đã bị rơi vào lỗ.
    """
    total = 0
    for b in potted_balls:
        if b.color == c:
            total += 1
    return total

def draw_potted_balls():
    """
    Hàm này được sử dụng để vẽ các quả bi đã bị rơi vào lỗ, đánh dấu các bi đã rơi vào lỗ.
    """
    for index in range(len(potted_balls)):
        gameDisplay.blit(potted_balls[index].sprite, (100000 + (index * 25), 1000000))

