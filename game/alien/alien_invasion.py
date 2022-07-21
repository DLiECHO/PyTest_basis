import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_fun as gf

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    initSet = Settings()
    # # 让gameFun模块获取游戏的初始数据
    # gf.get_set(initSet)
    screen = pygame.display.set_mode((initSet.screen_width, initSet.screen_height))
    pygame.display.set_caption(initSet.game_name)
    bg_color = [initSet.bg_initColor[0], initSet.bg_initColor[1], initSet.bg_initColor[2]]

    # 创建第一个外星人
    firstAlien = Ship(screen)

    # 创建一个用于编组的子弹
    waterDropGroup = Group()

    while True:

        # 监视鼠标和键盘
        gf.check_events(firstAlien)
        
        waterDropGroup.update()

        # 更新屏幕
        gf.update_screen(screen, firstAlien, bg_color)

run_game()