import pygame
from pygame.locals import *

# 定义屏幕宽、高
WIDTH = 480
HEIGHT = 600
FPS = 60

# 初始化
pygame.init()

# 初始化计时器
clock = pygame.time.Clock()

# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 创建Surface
# surf_plane = pygame.Surface((50, 50))
# 设置surf_plane的背景颜色
# surf_plane.fill((0, 255, 0))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # 完成精灵的初始化
        pygame.sprite.Sprite.__init__(self)
        # 初始化飞机精灵的图像，也就是长什么样
        self.image = pygame.Surface((50, 50))
        # 初始化飞机精灵图像的颜色
        self.image.fill((0, 255, 0))
        # 角色的长方形
        self.rect = self.image.get_rect()
        #  设置长方形中心的x的值
        self.rect.centerx = WIDTH / 2
        #  设置长方形底的值
        self.rect.bottom = HEIGHT - 10

    def update(self):
        self.speedx = 0
        # 获取按键状态
        keys = pygame.key.get_pressed()
        # 如果左移键被按下
        if keys[pygame.K_LEFT]:
            # x轴上的速度设置为‐8
            self.speedx = -8
        # 如果右键被按下
        if keys[pygame.K_RIGHT]:
            # x轴上的速度设置为8
            self.speedx = 8
        # 设置角色的x轴坐标
        self.rect.x += self.speedx
        # 边缘检测，如果碰到边缘，就停止不动
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


player = Player()
running = True
while running:
    # 设置游戏频率
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 结束游戏
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # 结束游戏
                running = False
    player.update()

    # 绘制屏幕的背景颜色
    screen.fill((0, 0, 0))

    # 将正方形绘制到屏幕上
    screen.blit(player.image, player.rect)

    # 重绘游戏界面，相当于刷新一次
    pygame.display.flip()
pygame.quit()
