import pygame
import math
import time
import sys
from components.PoolTable import draw_background
from components.GameState import *
from components.Collisions import *
from config import *
import components.screens.PauseMenu as PauseMenu
import config

pygame.init()

winner = None

def game_over(winner):
    """
    Hiển thị màn hình kết thúc trò chơi.

    Tham số:
    - winner: Người chơi chiến thắng.
    """
    import components.screens.GameOverMenu as GameOverMenu
    import config

    config.game_is_paused = True
    GameOverMenu.draw(winner)

# Vòng lặp chính của trò chơi
while True:
    draw_background()
    gameDisplay.blit(config.Fonts.basic.render('PLAYER ' + str(player_turn.number) + '\'S TURN', 1, Colors.WHITE), (600, 10))
    draw_potted_balls()
    for ball in balls:
        # Bỏ qua các quả bi đã rơi vào lỗ
        if ball.potted:
            continue

        gameDisplay.blit(ball.sprite, (ball.x - 18, ball.y - 18))

        # Không có gì cần thực hiện nếu quả bi không còn trong trò chơi
        if not in_play:
            continue

        # Di chuyển quả bi theo hướng và tốc độ
        if ball.speed > 0:
            for i in range(int(ball.speed)):
                # Xử lý va chạm với các bức tường và lỗ
                if ball.y - 18 <= 150 or ball.y + 18 >= 650 or ball.x + 18 >= 1200 or ball.x - 18 <= 200:
                    hit_sound.play()
                    if ball.speed > 1:
                        ball.speed -= 1
                    ball.movement_direction = collision_with_wall(
                        ball.x, ball.y, ball.movement_direction)
                    collision_monitor_reset()
                ball.x, ball.y = angle_to_coordinates(
                    ball.x, ball.y, ball.movement_direction, 1)
                
            # Kiểm tra nếu quả bi vào lỗ
            if ball_potted(ball.x, ball.y):
                sunk_sound.play()
                recent_potted_balls.append(ball)
                potted_balls.append(ball)
                ball.potted = True
            
            # Kiểm tra va chạm với các quả bi khác
            ball_collided_with = check_collision_with_other_ball(
                ball.x, ball.y, ball)
            if ball_collided_with is not None:  
                hit_sound.play()
                if first_ball_collided_with is None:
                    first_ball_collided_with = ball_collided_with
                ball.movement_direction, ball_collided_with.movement_direction, ball.speed, ball_collided_with.speed = ball_collision_physics(
                    ball.x, ball.y, ball_collided_with.x, ball_collided_with.y, ball.movement_direction, ball.speed)
                collision_monitor_reset()
                ball.collision_monitor[balls.index(
                    ball_collided_with)] = True
                ball_collided_with.collision_monitor[balls.index(
                    ball)] = True

            # Ma sát của bi
            if ball.frames >= (-30) * math.log10(0.05 * (ball.speed + 1)):
                ball.speed -= 0.5
                ball.frames = 0
            ball.frames += 1

            # Cập nhật vị trí của gậy    
            if ball is cue_ball:
                pool_cue_coords = (cue_ball.x - 462, cue_ball.y - 450)
        
        # Kiểm tra nếu tất cả các quả bi đã dừng lại
        if not balls_stopped():
            continue

        draw_background()
        draw_potted_balls()
        for ball in balls:
            if not ball.potted:
                gameDisplay.blit(ball.sprite, (ball.x - 18, ball.y - 18))
        pygame.display.update()
        time.sleep(0.5)

        # Kiểm tra xem có bao nhiêu quả bi đã rơi vào lỗ
        stripes, solids = 0, 0
        for ball in recent_potted_balls:
            """
            - Biến 'stripes' được tăng lên khi một quả bi sọc được rơi vào lỗ.
            - Biến 'solids' được tăng lên khi một quả bi trơn được rơi vào lỗ.
            - Các quả bi sọc và quả bi trơn đều được đánh số từ 1 đến 7.
            - recent_potted_balls: Danh sách các quả bi mới rơi vào lỗ.
            - config.initial_break: Cờ đánh dấu lượt đầu tiên của trò chơi.
            - player_turn: Người chơi đang có lượt chơi.
            - player_1, player_2: Đối tượng người chơi 1 và người chơi 2.
            """
            if ball.color == 'stripes':
                stripes += 1
                if config.initial_break:
                    config.initial_break = False
                    turn_change = False
                    if player_turn.number == 1:
                        player_1.color = 'stripes'
                        player_2.color = 'solids'
                    elif player_turn.number == 2:
                        player_2.color = 'stripes'
                        player_1.color = 'solids'
            elif ball.color == 'solids':
                solids += 1
                if config.initial_break:
                    config.initial_break = False
                    turn_change = False
                    if player_turn.number == 1:
                        player_1.color = 'solids'
                        player_2.color = 'stripes'
                    elif player_turn.number == 2:
                        player_2.color = 'solids'
                        player_1.color = 'stripes'
            elif ball.color == 'eight':
                """
                Xác định người chơi chiến thắng khi quả bi số 8 được rơi vào lỗ.
                - Nếu một người chơi chỉ còn lại quả bi số 8 trên bàn và họ không làm cho quả bi này vào lỗ hoặc làm cho nó vào lỗ sai, người chơi đó thua cuộc.
                - Trong trường hợp cả hai người chơi còn lại vẫn chơi và quả bi số 8 bị rơi vào lỗ do người chơi khác, người chơi có quả bi số 8 sẽ thắng.
                - Ngược lại, nếu quả bi số 8 được đánh vào lỗ đúng bởi người chơi có quả bi này, người chơi đó thắng.
                """
                if player_turn.only_eight_ball_left:
                    if cue_ball.potted or not first_ball_collided_with.color == 'eight':
                        if player_turn.number == 1:
                            winner = player_2
                        else:
                            winner = player_1
                    else:
                        winner = player_turn
                else:
                    if player_turn.number == 1:
                        winner = player_2
                    else:
                        winner = player_1
                game_over(winner)
        recent_potted_balls[:] = []

        # Kiểm tra xem có cần thay đổi lượt chơi 
        if player_turn.only_eight_ball_left:
            turn_change = True
            cue_ball_in_hand = False
            if first_ball_collided_with is not None:
                if not first_ball_collided_with.color == 'eight':
                    cue_ball_in_hand = True
            else:
                cue_ball_in_hand = True
        else:
            if player_turn.color == 'stripes':
                if stripes > 0:
                    turn_change = False
                else:
                    turn_change = True
            elif player_turn.color == 'solids':
                if solids > 0:
                    turn_change = False
                else:
                    turn_change = True
            if first_ball_collided_with is not None:
                if player_turn.color == 'stripes' and not first_ball_collided_with.color == 'stripes':
                    turn_change = True
                    cue_ball_in_hand = True
                elif player_turn.color == 'solids' and not first_ball_collided_with.color == 'solids':
                    turn_change = True
                    cue_ball_in_hand = True
            else:
                turn_change = True
                cue_ball_in_hand = True
            if number_of_balls_potted(player_turn.color) == 7:
                player_turn.only_eight_ball_left = True
        first_ball_collided_with = None
        if cue_ball.potted:
            potted_balls.remove(cue_ball)
            turn_change = True
            cue_ball.potted = False
            cue_ball_in_hand = True

        if turn_change:
            player_turn = player_turn_switch(player_turn)
        if cue_ball_in_hand:
            ball_in_hand()
            pool_cue_coords = (cue_ball.x - 462, cue_ball.y - 450)
            cue_ball_in_hand = False

        in_play = False

    # Vẽ gậy và hướng dẫn 
    if not in_play:
        if draw_guide:
            pygame.draw.line(gameDisplay, 
                             Colors.WHITE,
                             (cue_ball.x, cue_ball.y),
                             mouse_hold_coords, 
                             2
                            )
            gameDisplay.blit(pool_cue_rotated, pool_cue_coords)
            pygame.draw.circle(gameDisplay, Colors.WHITE, mouse_hold_coords, 16, 1)

        # Xử lý hướng và tốc độ của quả bi
        if mouse_held:
            mouseX, mouseY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            temporary_angle = cue_direction + 180
            if temporary_angle > 360:
                temporary_angle -= 360
            strike_distance = distance_between_points(
                mouse_hold_coords[0], mouse_hold_coords[1], mouseX, mouseY)
            if strike_distance > 210:
                strike_distance = 210
            pool_cue_coords = angle_to_coordinates(
                cue_ball.x - 462, cue_ball.y - 450, temporary_angle, strike_distance)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Tạm dừng trò chơi
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                config.game_is_paused = not config.game_is_paused
                PauseMenu.draw_pause_menu()

        # Xử lý sự kiện nhấn chuột
        if in_play:
            continue

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_hold_coords = pygame.mouse.get_pos()
            mouse_held = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if config.prevent_shoot:
                config.prevent_shoot = False
                break
            mouse_held = False
            if strike_distance > 16:
                cue_ball.speed = round((strike_distance - 16)/16)
                in_play = True
                draw_guide = False
                strike_sound.play()
            cue_ball.movement_direction = cue_direction
            collision_monitor_reset()
        elif event.type == pygame.MOUSEMOTION and mouse_held is False:
            draw_guide = True
            mouseX, mouseY = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
            mouse_hold_coords = mouseX, mouseY
            cue_direction = coordinates_to_angle(
                cue_ball.x, cue_ball.y, mouseX, mouseY)
            pool_cue_rotated = rot_center(pool_cue_original, cue_direction)
            pool_cue_coords = (cue_ball.x - 462, cue_ball.y - 450)

    pygame.display.update()
    pygame.time.Clock().tick(60)
