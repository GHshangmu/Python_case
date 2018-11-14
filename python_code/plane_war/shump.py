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

# 初始化mixer模块
pygame.mixer.init()

# 加载子弹发生的声音
shoot_sound = pygame.mixer.Sound('snd/shoot.wav')

# 加载子弹碰撞上陨石的声音
meteorite_bullet_hit_sounds = []
for snd in ['meteorite_bullet_hit_01.wav', 'meteorite_bullet_hit_02.wav']:
    meteorite_bullet_hit_sounds.append(pygame.mixer.Sound('snd/'+snd))

# 定义游戏的背景音乐
pygame.mixer.music.load('snd/music_bg.mp3')

# 创建屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 创建Surface
# surf_plane = pygame.Surface((50, 50))
# 设置surf_plane的背景颜色
# surf_plane.fill((0, 255, 0))

# 定义陨石列表
meteor_list = ['img_meteorite_01.png', 'img_meteorite_02.png', 'img_meteorite_03.png',
               'img_meteorite_04.png', 'img_meteorite_05.png', 'img_meteorite_06.png',
               'img_meteorite_07.png', 'img_meteorite_08.png']

# 循环获取所有图片
meteor_images = []
for img in meteor_list:
    meteor_images.append(pygame.image.load('img/' + img))


# 定义绘制计分的方法
def draw_text(surf, text, size, x, y):
    # 设置画笔的字体
    font_name = pygame.font.match_font('arial')
    # 设置画笔的字体和大小
    font = pygame.font.Font(font_name, size)
    # 绘制内容：text为内容，True为是否抗锯齿，字体颜色为白色
    text_surface = font.render(text, True, (255, 255, 255))
    # 设置字体的矩形
    text_rect = text_surface.get_rect()
    # 设置字体的位置
    text_rect.midtop = (x, y)
    # 将字体绘制到屏幕上
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # 完成精灵的初始化
        pygame.sprite.Sprite.__init__(self)

        # 初始化飞机精灵的图像，也就是长什么样
        # self.image = pygame.Surface((50, 50))
        # 初始化飞机精灵图像的颜色
        # self.image.fill((0, 255, 0))

        # 初始化飞机精灵的图像，也就是长什么样
        self.image = pygame.image.load(r'C:\Users\m_sha\Desktop\u盘\Work File 7.3\File 1\Python\pygame\resource\particle\wsparticle_test_001.png')

        # 角色的长方形
        self.rect = self.image.get_rect()

        # 把飞机当圆处理，设置飞机圆的半径
        self.radius = 20
        # pygame.draw.circle(self.image, (0, 255, 0), self.rect.center, self.radius)

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
        # 调用发射子弹的声音
        shoot_sound.play()


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
        # self.image = pygame.image.load('img\img_meteorite.png')

        # 随机获取列表中的某一项
        self.image = random.choice(meteor_images)

        # 获取陨石的长方形
        self.rect = self.image.get_rect()

        # 把陨石当做圆处理，设定陨石的半径
        self.radius = int(self.rect.width * 0.85 / 2)
        # pygame.draw.circle(self.image, (0, 255, 0), self.rect.center, self.radius)

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

        self.image = pygame.image.load(r'C:\Users\m_sha\Desktop\u盘\Work File 7.3\File 1\Python\pygame\resource\
        particle\wsparticle_tailinga_0.png')

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

score = 0
running = True
# 循环播放背景音乐
pygame.mixer.music.play(loops=-1)

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
        # 分数增加
        score += 5
        # 随机选择音效
        random.choice(meteorite_bullet_hit_sounds).play()

        meteorite = Meteorite()
        all_sprites.add(meteorite)
        all_meteorite.add(meteorite)

    # 检测飞机和陨石之间的碰撞
    hits = pygame.sprite.spritecollide(player, all_meteorite, True, pygame.sprite.collide_circle)
    # 如果碰撞，则游戏结束
    if hits:
        running = False

    # 绘制屏幕的背景颜色
    # screen.fill((0, 0, 0))

    background = pygame.image.load(r"C:\Users\m_sha\Desktop\u盘\Work File 7.3\File 1\Python\pygame\
    resource\飞机大战四套\2\img_bg_level_3.jpg").convert()
    screen.blit(background, background.get_rect())

    # 将正方形绘制到屏幕上
    # screen.blit(player.image, player.rect)

    # 将精灵组中的所有精灵都绘制到屏幕
    all_sprites.draw(screen)

    # 绘制分数
    draw_text(screen, str(score), 18, WIDTH / 2, 10)

    # 重绘游戏界面，相当于刷新一次
    pygame.display.flip()
pygame.quit()
