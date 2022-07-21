import pygame

class Ship():

    def __init__(self, screen: pygame.Surface):
        '''初始化飞船并设置其初始位置'''

        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('image/aliensP1.png')
        # self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 控制移动的标志
        self.move_right = False
        self.move_up = False
        self.move_left = False
        self.move_down = False

        # 飞船移动的基础速度
        self.speed = 1.2

        # 飞船的带小数的位置参数，就是说ship实际上一直在float层面上移动
        # 但是pygame的rect位置不接受float，所以在渲染的时候还是只接受整数部分
        # 不过假设speed=1.3，移动了1/2/3次时，即1.3/2.6/3.9，rect虽然只显示在1/2/3
        # 仿佛每次都丢失了精度，但其实它在背后一直默默努力，小数的积累终于在第4次爆发
        # 第4次，rect终于不再是平凡的前进到4，它直接跳到了5
        # 向伟大的渺小致敬：1.3/2.6/3.9/5.2 ——> 1/2/3/5
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)

    def showShip(self):
        self.screen.blit(self.image, self.rect)

    def shipRun(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.centerX += self.speed
            self.rect.centerx = self.centerX
            if self.rect.right > self.screen_rect.right:
                self.centerX = self.screen_rect.right
                self.rect.right = self.screen_rect.right

        if self.move_up and self.rect.top > 0:
            self.centerY -= self.speed
            self.rect.centery = self.centerY
            if self.rect.top < 0:
                self.rect.top = 0
                self.centerY = 0

        if self.move_left and self.rect.left > 0:
            self.centerX -= self.speed
            self.rect.centerx = self.centerX
            if self.rect.left < 0:
                self.rect.left = 0
                self.centerX = 0

        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += self.speed
            self.rect.centery = self.centerY
            if self.rect.bottom > self.screen_rect.bottom:
                self.rect.bottom = self.screen_rect.bottom
                self.centerY = 0
                
        # 上面把飞船的显示完全限制在框内，不让其因为飞船速度值，
        # 出现飞船整个直接一步出框，或者半边出框的情况
        # 但是这段代码颇为消耗时间，很多时候无需执行