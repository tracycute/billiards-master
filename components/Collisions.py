import pygame
import math
from .Ball import Ball
import config

def distance_between_points(x1, y1, x2, y2):
    """
    Tính khoảng cách giữa hai điểm trong không gian hai chiều.

    Tham số:
    - x1: Tọa độ x của điểm thứ nhất.
    - y1: Tọa độ y của điểm thứ nhất.
    - x2: Tọa độ x của điểm thứ hai.
    - y2: Tọa độ y của điểm thứ hai.

    Trả về:
    Khoảng cách giữa hai điểm được tính bằng cách sử dụng công thức Euclid.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def difference_between_angles(a1, a2):
    """
    Tính khoảng cách giữa hai góc trong đơn vị độ.

    Tham số:
    - a1: Góc thứ nhất (đơn vị độ).
    - a2: Góc thứ hai (đơn vị độ).

    Trả về:
    Khoảng cách giữa hai góc được tính bằng cách chọn góc nhỏ nhất giữa chúng.

     Ví dụ:
    - difference_between_angles(10, 350) sẽ trả về 20, vì khoảng cách nhỏ nhất là 20 độ.
    - difference_between_angles(180, 270) sẽ trả về 90, vì khoảng cách nhỏ nhất là 90 độ.

    """
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
    """
    Chuyển đổi tọa độ của hai điểm thành góc tương ứng (theo độ).

    Tham số:
    - x1: Tọa độ x của điểm thứ nhất.
    - y1: Tọa độ y của điểm thứ nhất.
    - x2: Tọa độ x của điểm thứ hai.
    - y2: Tọa độ y của điểm thứ hai.

    Trả về:
    Góc (theo độ) giữa hai điểm được tính dựa trên hệ tọa độ không gian hai chiều,
    trong đó góc được tính theo hướng ngược chiều kim đồng hồ từ trục x dương.

    Ví dụ:
    - coordinates_to_angle(0, 0, 1, 1) sẽ trả về 45, vì góc giữa (0,0) và (1,1) là 45 độ.
    - coordinates_to_angle(1, 1, 0, 0) sẽ trả về 225, vì góc giữa (1,1) và (0,0) là 225 độ.
    """
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
    """
    Chuyển đổi góc và độ dài thành tọa độ (x, y) của điểm cuối cùng.

    Tham số:
    - startx: Tọa độ x của điểm bắt đầu.
    - starty: Tọa độ y của điểm bắt đầu.
    - angle: Góc (theo độ) từ điểm bắt đầu đến điểm cuối cùng.
    - length: Độ dài của đoạn thẳng từ điểm bắt đầu đến điểm cuối cùng.

    Trả về:
    Một bộ tọa độ (x, y) của điểm cuối cùng, tính dựa trên góc và độ dài cho trước.
    Nếu góc là None, hàm sẽ trả về tọa độ của điểm bắt đầu.

    Ví dụ:
    - angle_to_coordinates(0, 0, 45, 1) sẽ trả về tọa độ của điểm cuối cùng khi di chuyển 1 đơn vị với góc 45 độ.
    - angle_to_coordinates(0, 0, None, 1) sẽ trả về tọa độ của điểm bắt đầu.
    """
    if angle is not None:
        return startx + length * math.cos(math.radians(angle)), starty - length * math.sin(math.radians(angle))
    else:
        return startx, starty

def rot_center(image, angle):
    """
    Xoay hình ảnh quanh tâm của nó.

    Tham số:
    - image: Hình ảnh cần được xoay.
    - angle: Góc xoay (theo độ).

    Trả về:
    Một hình ảnh đã được xoay theo góc được chỉ định.
    Hàm này xoay hình ảnh quanh tâm của nó và trả về hình ảnh mới đã được xoay.

    Ví dụ:
    - rot_center(image, 90) sẽ trả về hình ảnh đã được xoay 90 độ quanh tâm của nó.
    """
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

def collision_with_wall(x, y, angle):
    """
    Kiểm tra va chạm với các thành bi-a.

    Tham số:
    - x: Tọa độ x của quả bi.
    - y: Tọa độ y của quả bi.
    - angle: Góc di chuyển của quả bi.

    Trả về:
    Góc phản xạ sau khi va chạm với thành bi-a, tính từ trục x dương.
    Hàm này kiểm tra va chạm của quả bi với các thành bi-a và trả về góc phản xạ sau khi va chạm.

    """
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
    """
    Hàm này đặt lại trạng thái kiểm tra va chạm của tất cả các quả bi trong trò chơi 8 ball về False.
    """
    for b in config.balls: #update
        if not b.potted:
            for b2 in range(16):
                b.collision_monitor[b2] = False

def collision_monitor_reset_9():
    """
    Hàm này đặt lại trạng thái kiểm tra va chạm của tất cả các quả bi trong trò chơi 9 ball về False.
    """
    for b in config.balls_9: #update
        if not b.potted:
            for b2 in range(16):
                b.collision_monitor[b2] = False

def check_collision_with_other_ball(x, y, ball1):
    """
    Hàm này kiểm tra va chạm của quả bi với các quả bi khác và trả về quả bi gần nhất mà ball1 va chạm tới trong 8 ball.

    Tham số:
    - x: Tọa độ x của quả bi.
    - y: Tọa độ y của quả bi.
    - ball1: Quả bi cần kiểm tra.

    Trả về:
    Quả bi gần nhất mà ball1 va chạm với.
    """
    for b in config.balls: 
        if not ball1.collision_monitor[config.balls.index(b)] and not b.potted: # update
            if b.x != x and b.y != y:
                if distance_between_points(x, y, b.x, b.y) <= 35:
                    return b

def check_collision_with_other_ball_9(x, y, ball1):
    """
    Hàm này kiểm tra va chạm của quả bi với các quả bi khác và trả về quả bi gần nhất mà ball1 va chạm tới trong 9 ball.

    Tham số:
    - x: Tọa độ x của quả bi.
    - y: Tọa độ y của quả bi.
    - ball1: Quả bi cần kiểm tra.

    Trả về:
    Quả bi gần nhất mà ball1 va chạm tới.
    """
    for b in config.balls_9: # update
        if not ball1.collision_monitor[config.balls_9.index(b)] and not b.potted: # update
            if b.x != x and b.y != y:
                if distance_between_points(x, y, b.x, b.y) <= 35:
                    return b


def ball_collision_physics(x1, y1, x2, y2, initial_angle: float, initial_speed):
    """
    Hàm này tính toán vật lý của va chạm giữa hai quả bi và trả về các thông số cần thiết sau va chạm.

    Tham số:
    - x1: Tọa độ x của quả bi thứ nhất.
    - y1: Tọa độ y của quả bi thứ nhất.
    - x2: Tọa độ x của quả bi thứ hai.
    - y2: Tọa độ y của quả bi thứ hai.
    - initial_angle: Góc ban đầu của quả bi thứ nhất.
    - initial_speed: Tốc độ ban đầu của quả bi thứ nhất.

    Trả về:
    Một bộ các thông số gồm góc di chuyển của quả bi thứ nhất sau va chạm, góc di chuyển của quả bi thứ hai sau va chạm,
    tốc độ của quả bi thứ nhất sau va chạm và tốc độ của quả bi thứ hai sau va chạm.
    
    """
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

