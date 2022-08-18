import pygame
class Ship():
    def __init__(self,screen):
        """初始化飞船并设置其位置"""
        self.screen = screen
        """加载飞船图像并获取其外接矩形"""
        self.image = pygame.image.load("/Users/chikwongyip/PycharmProjects/pygame/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        """将每艘飞船放在屏幕底部中央"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

class Boss():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("/Users/chikwongyip/PycharmProjects/pygame/images/python.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)