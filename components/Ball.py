import pygame


class Ball (object):
    def __init__(self, color, x, y, img_name):
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
        self.movement_direction = 0
        self.speed = 0
        self.frames = 0
        self.potted = False
        for i in range(16):
            self.collision_monitor[i] = False
