class Settings():
    '''存储游戏的所有基本设置的类'''

    def __init__(self) -> None:
        '''初始化游戏设置'''
        
        #游戏名
        self.game_name = '三 体 入 侵'

        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_initColor = (0, 0, 0)