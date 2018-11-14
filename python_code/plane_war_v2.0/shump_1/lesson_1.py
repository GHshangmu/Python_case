import pygame
from pygame.locals import *

# 定义屏幕宽、高
WIDTH = 480
HEIGHT = 600

# 初始化
pygame.init()

# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 创建Surface
surf_plane = pygame.Surface((50, 50))

# 设置surf_plane的背景颜色
surf_plane.fill((0, 255, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 结束游戏
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # 结束游戏
                running = False
    # 将正方形绘制到屏幕上
    screen.blit(surf_plane, (100, 100))
    # 重绘游戏界面，相当于刷新一次
    pygame.display.flip()
pygame.quit()
