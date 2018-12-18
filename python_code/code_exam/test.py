import time
import pygame
from pygame.locals import *

# 定义屏幕宽、高
WIDTH = 480
HEIGHT = 480
# 初始化
pygame.init()
# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 创建Surface
surf_plane = pygame.Surface((50, 50))
# 设置surf_plane的背景颜色
surf_plane.fill((0, 255, 0))


def wait(second):
    time.sleep(second / 1000)


def play_sound(sound_name, is_loop):
    # 初始化mixer模块
    pygame.mixer.init()
    # 定义游戏的背景音乐
    pygame.mixer.music.load(sound_name)
    if is_loop == True:
        pygame.mixer.music.play(loops=-1)


def visible(is_visible, img):
    if is_visible == False:
        img.set_alpha(0)


def start():
    # 获取按键状态
    keys = pygame.key.get_pressed()
    # 如果左移键被按下
    if keys[pygame.K_SPACE]:
        # 等待一秒
        wait(5000)
        # 循环播放背景音乐
        play_sound(r'C:\Users\m_sha\Python_case\python_code\plane_war_v2.0\shump_6\snd/music_bg.mp3', True)
        visible(False, surf_plane)


if __name__ == "__main__":
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

        start()

        # 绘制屏幕的背景颜色
        screen.fill((0, 0, 0))
        # 将正方形绘制到屏幕上
        screen.blit(surf_plane, (100, 100))
            # 重绘游戏界面，相当于刷新一次
        pygame.display.flip()

    pygame.quit()
