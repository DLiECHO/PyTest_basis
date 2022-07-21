import pygame
from pygame.sprite import Sprite

from ship import Ship

class waterDrop(Sprite):
    """外星人发射的水滴"""

    def __init__(self, screen: pygame.Surface, alien: Ship) -> None:
        # 在外星人所在的位置创建一个水滴对象
        super().__init__()
        self.screen = screen

        # 设置飞船的攻击方式-水滴的基本形状
        self.waterDrop = pygame.image.load('image/waterDrop1.png')
        self.speed = 1.4
        self.rect = self.waterDrop.get_rect()

        # 定义水滴的位置
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.top

        # 用小数控制子弹的位置
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)

    def update(self) -> None:
        '''移动水滴'''
        self.centerY -= self.speed
        self.rect.centery = self.centerY

    def draw(self) -> None:
        '''在屏幕上显示水滴'''
        self.screen.blit(self.waterDrop, self.rect)