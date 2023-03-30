import pygame
from data import*


class Shooter(pygame.Rect):
    def __init__(self, x,  y, width, height, speed, image):
        super().__init__(x, y, width, height)
        self.IMAGE = image[0]
        self.IMAGE_LIST = image 
        self.SPEED = speed
        self.IMAGE_MOVE = 0

    def move_image(self):
        self.IMAGE = self.IMAGE_LIST[self.IMAGE_MOVE // 10]
        self.MOVE += 1
        if sellf.IMAGE_MOVE == 20:
            self.IMAGE_MOVE = 0

class Hero(Shooter):
        def __init__(self, x, y, width, height, speed, image):
            super().__init__(x, y , width, height, speed, image)
            self.MOVE = {"UP": False, "DOWN": False, "LEFT": False, "RIGHT": False}
            self.HP = 3
            self.POINT = 0
            self BULLETS = []
            self.BUULET_COUNTER = 0
            

    def move(self):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED