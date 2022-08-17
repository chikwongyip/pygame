import sys
import pygame
import game_functions as gf
from setting import Settings
from ship import Ship
def run_game():
    """初始化游戏"""
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    """开始游戏"""
    while True:
        gf.check_events()
        gf.update_screen(ai_setting, screen, ship)
        screen.fill(ai_setting.bg_color)
        ship.blitme()
        ship.blitme()
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.flip()

run_game()