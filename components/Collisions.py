import pygame
import math
from .Ball import Ball
import config

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def difference_between_angles(a1, a2):
    distance1, distance2 = abs(a1 - a2), abs(a2 - a1)
    if distance1 <= 180:
        return distance1
    elif distance2 <= 180:
        return distance2
    else:
        if a1 > a2:
            return 360 - a1 + a2
        else:
            return 360 - a2 + a1

def coordinates_to_angle(x1, y1, x2, y2):
    x_diff, y_diff = x2 - x1, -(y2 - y1)
    if x_diff == 0:
        if y_diff > 0:
            return 90
        elif y_diff < 0:
            return 270
        else:
            return 0
    else:
        beta = math.degrees(math.atan(y_diff/x_diff))

    if x_diff > 0:
        if y_diff < 0:
            beta += 360
    elif x_diff < 0:
        beta += 180
    return beta

def angle_to_coordinates(startx, starty, angle, length):
    if angle is not None:
        return startx + length * math.cos(math.radians(angle)), starty - length * math.sin(math.radians(angle))
    else:
        return startx, starty

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def collision_with_wall(x, y, angle):
    if y - 18 <= 150 or y + 18 >= 650:
        return 360 - angle
    elif x + 18 >= 1200:
        if angle < 90:
            return 180 - angle
        elif angle > 270:
            return 540 - angle
    elif x - 18 <= 200:
        if 180 > angle > 90:
            return 180 - angle
        elif 270 > angle >= 180:
            return 540 - angle

def collision_monitor_reset():
    for b in config.balls: #update
        if not b.potted:
            for b2 in range(16):
                b.collision_monitor[b2] = False

def collision_monitor_reset_9():
    for b in config.balls_9: #update
        if not b.potted:
            for b2 in range(16):
                b.collision_monitor[b2] = False

def check_collision_with_other_ball(x, y, ball1):
    for b in config.balls: 
        if not ball1.collision_monitor[config.balls.index(b)] and not b.potted: # update
            if b.x != x and b.y != y:
                if distance_between_points(x, y, b.x, b.y) <= 35:
                    return b

def check_collision_with_other_ball_9(x, y, ball1):
    for b in config.balls_9: # update
        if not ball1.collision_monitor[config.balls_9.index(b)] and not b.potted: # update
            if b.x != x and b.y != y:
                if distance_between_points(x, y, b.x, b.y) <= 35:
                    return b


def ball_collision_physics(x1, y1, x2, y2, initial_angle: float, initial_speed):
    angle2 = coordinates_to_angle(x1, y1, x2, y2)
    clockwise, counter_clockwise = angle2 - 90, angle2 + 90
    if difference_between_angles(clockwise, initial_angle) < difference_between_angles(counter_clockwise, initial_angle):
        angle1 = clockwise
    else:
        angle1 = counter_clockwise
    speed1 = initial_speed * math.cos(math.radians(difference_between_angles(angle1, initial_angle)))
    speed2 = initial_speed * math.cos(math.radians(difference_between_angles(angle2, initial_angle)))
    if speed1 < 1:
        speed1 = 1
    if speed2 < 1:
        speed2 = 1
    return angle1, angle2, speed1, speed2

