import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其位置"""
        self.screen = screen
        """加载设置"""
        self.ai_settings = ai_settings
        """加载飞船图像并获取其外接矩形"""
        """mac setting"""
        self.image = pygame.image.load("/Users/chikwongyip/PycharmProjects/pygame/images/ship.bmp")
        """windows setting"""
        #self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        """将每艘飞船放在屏幕底部中央"""
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        
        #self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

class Boss():
    def __init__(self,screen):
        self.screen = screen
        """mac setting"""
        #self.image = pygame.image.load("/Users/chikwongyip/PycharmProjects/pygame/images/python.jpg")
        """windows setting"""
        self.image = pygame.image.load("images\python.jpg")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)