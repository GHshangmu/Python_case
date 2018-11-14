import random
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
        # self.image = pygame.Surface((50, 50))
        # 初始化飞机精灵图像的颜色
        # self.image.fill((0, 255, 0))

        # 初始化飞机精灵的图像，也就是长什么样
        self.image = pygame.image.load("img/img_plane.png")

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

    # 添加射击的功能
    def shoot(self):
        # 定义子弹
        bullet = Bullet(self.rect.centerx, self.rect.top)
        # 将子弹加入全部精灵组和子弹精灵组
        all_sprites.add(bullet)
        all_bullets.add(bullet)


# 陨石精灵
class Meteorite(pygame.sprite.Sprite):
    def __init__(self):
        # 初始化
        pygame.sprite.Sprite.__init__(self)

        # 定义陨石的图形
        # self.image = pygame.Surface((30, 40))
        # 定义陨石的颜色
        # self.image.fill((255, 0, 0))

        # 定义陨石的图形
        self.image = pygame.image.load("img\img_meteorite.png")
        # 获取陨石的长方形
        self.rect = self.image.get_rect()
        # 设置陨石出现的x轴坐标:随机出现在0~屏幕宽度‐陨石本身宽度的位置
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # y轴坐标
        self.rect.y = random.randrange(-100, -40)
        # y轴速度
        self.speedy = random.randrange(1, 8)
        # x轴速度
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -30 or self.rect.right > WIDTH + 30:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)


# 子弹
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        # self.image = pygame.Surface((10, 20))
        # self.image.fill((255, 255, 0))

        self.image = pygame.image.load("img/img_bullet.png")

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        # 设置子弹的速度，子弹是从下往上的，所以为负
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy


# 定义玩家飞机对象
player = Player()
# 定义全部精灵组
all_sprites = pygame.sprite.Group()

# 将飞机加入精灵组
all_sprites.add(player)
# 定义陨石精灵组
all_meteorite = pygame.sprite.Group()
# 定义子弹精灵组
all_bullets = pygame.sprite.Group()

# 定义8个陨石并加入到精灵组all_sprites
for i in range(8):
    met = Meteorite()
    all_sprites.add(met)
    all_meteorite.add(met)
running = True
while running:
    # 设置游戏频率
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 结束游戏
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_ESCAPE:
                # 结束游戏
                running = False
    # player.update()
    all_sprites.update()

    hits = pygame.sprite.groupcollide(all_meteorite, all_bullets, True, True)
    # 如果碰撞了，则重新生成一个陨石，并加入到all_sprites和all_meteorite精灵组
    for hit in hits:
        meteorite = Meteorite()
        all_sprites.add(meteorite)
        all_meteorite.add(meteorite)

    # 检测飞机和陨石之间的碰撞
    hits = pygame.sprite.spritecollide(player, all_meteorite, True)
    # 如果碰撞，则游戏结束
    if hits:
        running = False

    # 绘制屏幕的背景颜色
    # screen.fill((0, 0, 0))

    background = pygame.image.load("img/img_bg.jpg").convert()
    screen.blit(background, background.get_rect())

    # 将正方形绘制到屏幕上
    # screen.blit(player.image, player.rect)

    # 将精灵组中的所有精灵都绘制到屏幕
    all_sprites.draw(screen)

    # 重绘游戏界面，相当于刷新一次
    pygame.display.flip()
pygame.quit()
