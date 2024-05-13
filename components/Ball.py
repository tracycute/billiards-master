import pygame


class Ball (object):
    def __init__(self, color, x, y, img_name):
        """
        Khởi tạo một đối tượng bóng.

        Tham số:
        - color: Màu sắc của bóng.
        - x: Tọa độ x của bóng trên màn hình.
        - y: Tọa độ y của bóng trên màn hình.
        - img_name: Tên của tập tin hình ảnh đại diện cho bóng.

        Thuộc tính:
        - color: Màu sắc của bóng.
        - sprite: Hình ảnh của bóng.
        - x: Tọa độ x của bóng trên màn hình.
        - y: Tọa độ y của bóng trên màn hình.
        - movement_direction: Hướng di chuyển của bóng.
        - speed: Tốc độ di chuyển của bóng.
        - frames: Số khung hình đã trôi qua.
        - potted: Trạng thái của bóng (đã vào lỗ hay chưa).
        - collision_monitor: Mảng đánh dấu va chạm với các quả bóng khác.
        """
        self.color = color
        ball_img = pygame.image.load(img_name).convert_alpha()
        self.sprite = pygame.transform.scale(ball_img, (36, 36))

        self.x = x
        self.y = y
        
        self.movement_direction = 0
        self.speed = 0
        self.frames = 0
        self.potted = False
        self.collision_monitor = []
        for i in range(16):
            self.collision_monitor.append(False)

    def reset_state(self):
        """
        Đặt lại trạng thái của đối tượng bóng.

        Phương thức này đặt lại các thuộc tính của đối tượng bóng về trạng thái ban đầu.

        Các thuộc tính được đặt lại:
        - movement_direction: Hướng di chuyển của bóng.
        - speed: Tốc độ di chuyển của bóng.
        - frames: Số khung hình đã trôi qua.
        - potted: Trạng thái của bóng (đã vào lỗ hay chưa).
        - collision_monitor: Mảng đánh dấu va chạm với các quả bóng khác.
        """
        self.movement_direction = 0
        self.speed = 0
        self.frames = 0
        self.potted = False
        for i in range(16):
            self.collision_monitor[i] = False
