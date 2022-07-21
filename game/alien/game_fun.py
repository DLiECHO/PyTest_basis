import sys
import pygame
from pygame.sprite import Group

from ship import Ship
import bg_color_change as bgc
from ship_waterDrop import waterDrop

# bg_color = [100,100,100]
# def get_set(set: Settings):
#     global bg_color
#     bg_color = [set.bg_initColor[0], set.bg_initColor[1], set.bg_initColor[2]]

# 检测键盘按下（外星人移动、发射攻击）
def check_keydown_event(event, alien: Ship, waterDropGroup: Group, screen: pygame.surface):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        alien.move_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        alien.move_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        alien.move_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        alien.move_down = True
    elif event.key == pygame.K_SPACE:
        newWaterDrop = waterDrop(screen, alien)

# 检测键盘按键抬起（外星人移动、发射攻击）
def check_keyup_event(event, alien: Ship, waterDropGroup: Group):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        alien.move_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        alien.move_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        alien.move_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        alien.move_down = False

# 检测鼠标（外星人发射攻击事件）

# 检测鼠标、键盘事件并作出响应
def check_events(alien: Ship):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():

        # 外星人移动
        if event.type == pygame.KEYDOWN:
            check_keydown_event(event, alien)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, alien)

        elif event.type == pygame.QUIT:
            sys.exit('退出游戏')
    
    alien.shipRun()
    

def update_screen(screen: pygame.Surface, alien: Ship, bg_color: list):
        # 颜色渐变函数
        bgc.colorChange(bg_color)
        screen.fill(bg_color)
        # print(bg_color)

        # 让最近绘制的屏幕可见
        alien.showShip()
        pygame.display.flip()