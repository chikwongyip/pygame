from ast import If
import curses
import sys
import pygame
def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEY_DOWN:
            if event.key == pygame.K_RIGHT:
                #向右飞
                ship.rect.centerx += 1
def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都会重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()