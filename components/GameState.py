import pygame
import sys
from config import *
from .Collisions import *
from .PoolTable import draw_background
from .Player import *
def player_turn_switch(turn):
    if turn.number == 1:
        return player_2
    elif turn.number == 2:
        return player_1

def balls_stopped():
    for ball in balls: 
        if ball.speed > 0 and not ball.potted:
            return False
    return True

def balls_stopped_9():
    for ball in balls_9:
        if ball.speed > 0 and not ball.potted:
            return False
    return True

def ball_potted(x, y):
    for hole in holes:
        if distance_between_points(x, y, hole[0], hole[1]) < 30:
            return True
    return False

def ball_in_hand():
    ball_dropped = False
    button_down = False
    while not ball_dropped:
        draw_background()
        draw_potted_balls()
        for ball in balls:
            if not ball.potted: gameDisplay.blit(ball.sprite, (ball.x - 18, ball.y - 18))
        pygame.display.update()
        for e in pygame.event.get():
            # if e.type == pygame.QUIT:
            #     pygame.quit()
            #     sys.exit()
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
    total = 0
    for b in potted_balls:
        if b.color == c:
            total += 1
    return total

def draw_potted_balls():
    for index in range(len(potted_balls)):
        gameDisplay.blit(potted_balls[index].sprite, (100000 + (index * 25), 1000000))

