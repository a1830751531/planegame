import pygame
from pygame.locals import *
import sys

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
    def display(self):
        '''
        把自己展示出来
        :return:
        '''
        self.window.blit(self.surface,(self.x,self.y))

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

while True:
    #展示在窗口
    window.blit(bg,(0,0))
    #展示飞机
    plane.display()
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