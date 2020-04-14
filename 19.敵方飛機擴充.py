import pygame
from pygame.locals import *
import sys
import random

"""----------------- 敌方飞机类 -----------------"""
class EnemyPlane:
    def __init__(self,window):
        #需要展示的窗口
        self.window = window
        #重置
        self.reset()

    def reset(self):
        #展示的surface
        self.surface = pygame.image.load('img/img-plane_{}.png'.format(random.randint(1,7)))
        #飛機的寬度和高度
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        #坐標
        self.x = random.randint(0,windowW-self.width)
        self.y = -self.height

    def display(self):
        self.window.blit(self.surface,(self.x,self.y))
        #自動移動
        self.y += 1
        #如果飛機超出窗口就重置
        if self.y > windowH:
            self.reset()

"""----------------- 提取子弹类 -----------------"""
class Bullet:
    def __init__(self,window,px,py,pw):
        #需要展示的窗口
        self.window = window
        #展示的surface
        self.surface = pygame.image.load('img/bullet_10.png')
        #子弹的高度宽度
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        #坐标
        self.x = px + (pw - self.width) / 2
        self.y = py - self.height / 2

    def display(self):
        self.window.blit(self.surface,(self.x,self.y))
        #自動移動
        self.y -= 2

    def needDestroy(self):
        return self.y < -self.height

    def hasCollision(self,enemy):
        '''
        判断子弹是否和飞机发生了碰撞
        @:param enemy 敌方飞机
        :return:
        '''
        #子彈矩形
        bulletRect = pygame.Rect(self.x, self.y, self.width, self.height)
        #敵方飛機矩形
        enemyRect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        return bulletRect.colliderect(enemyRect)

"""----------------- 抽取我方飞机类 -----------------"""
"""
飞机:
属性: 显示的窗口  x y 
行为: 把自己展示到窗口上
"""
'''
按压事件:按下不松手会一直执行
按下事件:按下不松手只会执行一次
'''
class Plane:
    def __init__(self,window,x,y):
        #需要展示的窗口
        self.window = window
        #坐标
        self.x = x
        self.y = y
        #展示的surface
        self.surface = pygame.image.load('img/hero2.png')
        #飞机的高度宽度
        self.width = self.surface.get_width()
        self.height = self.surface.get_height()
        #发射子弹的列表
        self.bullets = []
        self.hp = 5

    def hasCollision(self,enemy):
        '''
        判断敵方飛機是否和飞机发生了碰撞
        @:param enemy 敌方飞机
        :return:
        '''
        #我方飛機矩形
        planeRect = pygame.Rect(self.x, self.y, self.width, self.height)
        #敵方飛機矩形
        enemyRect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        return planeRect.colliderect(enemyRect)

    def display(self):
        '''
        把自己展示出来
        :return:
        '''
        print(len(self.bullets))
        self.window.blit(self.surface,(self.x,self.y))

        #判斷我方飛機是否和敵方飛機發生了碰撞
        for enemy in enemyList:
            if self.hasCollision(enemy):
                #敵方飛機重置
                enemy.reset()
                #我方飛機掉血
                self.hp -= 1
                #跳出循環
                break
        print('血量',self.hp)
        #是否發生碰撞
        for bullet in self.bullets:
            for enemy in enemyList:
                if bullet.hasCollision(enemy):
                    self.bullets.remove(bullet)
                    enemy.reset()
                    break
        #判斷子彈是否需要銷毀
        for bullet in self.bullets:
            if bullet.needDestroy():
                print('需要銷毀')
                #需要銷毀
                self.bullets.remove(bullet)
            else:#展示子彈
                bullet.display()

        #把飞机发射的子弹都展示出来
        # for bullet in self.bullets:
        #     #展示子弹
        #     bullet.display()

    def fire(self):
        #创建子弹对象
        bullet = Bullet(self.window,self.x,self.y,self.width)
        #添加子弹到bullet容器中
        self.bullets.append(bullet)
        #显示子弹

    def moveLeft(self):
        self.x -= 1
        #越界处理
        if self.x < 0:
            self.x = 0

    def moveRight(self):
        self.x += 1
        #越界处理
        if self.x > windowW - self.width:
            self.x = windowW - self.width

    def moveUp(self):
        self.y -= 1
        #越界处理
        if self.y < 0:
            self.y = 0

    def moveDown(self):
        self.y += 1
        #越界处理
        if self.y > windowH - self.height:
            self.y = windowH - self.height

#定義敵方飛機容器
enemyList = []
#初始化
pygame.init()

#加载背景
bg = pygame.image.load('img/img_bg_level_1.jpg')
#获取背景的高度宽度
bgW = bg.get_width()
bgH = bg.get_height()
#创建窗口
window = pygame.display.set_mode((bgW,bgH))
#获取窗口的高度宽度
windowW = window.get_width()
windowH = window.get_height()
#图标和标题
pygame.display.set_caption('飞机大战')
#图标
icon = pygame.image.load('img/app.ico')
pygame.display.set_icon(icon)

#加载飞机
plane = Plane(window,200,600)
#創建敵方飛機對象
for index in range(0,5):
    #創建敵方飛機
    enemy = EnemyPlane(window)
    #添加到容器中
    enemyList.append(enemy)


while True:

    #展示在窗口
    window.blit(bg,(0,0))
    #展示飞机
    plane.display()
    enemy.display()
    #刷新
    pygame.display.flip()
    #退出事件
    eventList = pygame.event.get()
    #遍历事件
    for event in eventList:
        if event.type == QUIT:
            #退出游戏
            pygame.quit()
            #退出程序
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                plane.fire()
        # elif event.type == KEYDOWN:
        #     if event.key == K_a:
        #         plane.moveLeft()
        #     if event.key == K_d:
        #         plane.moveRight()
        #     if event.key == K_w:
        #         plane.moveUp()
        #     if event.key == K_s:
        #         plane.moveDown()
    #监听按压事件 返回键盘当时的状态    0没有按压 1有按压
    status = pygame.key.get_pressed()
    #如果元组中有1
    if 1 in status:
        if status[K_a]:
            plane.moveLeft()
        elif status[K_d]:
            plane.moveRight()
        elif status[K_w]:
            plane.moveUp()
        elif status[K_s]:
            plane.moveDown()