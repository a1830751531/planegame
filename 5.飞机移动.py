import pygame
from pygame.locals import *
import sys

"""----------------- 抽取我方飞机类 -----------------"""
"""
飞机:
属性: 显示的窗口  x y 
行为: 把自己展示到窗口上
"""
class Plane:
    def __init__(self,window,x,y):
        #需要展示的窗口
        self.window = window
        #坐标
        self.x = x
        self.y = y
        #展示的surface
        self.surface = pygame.image.load('img/hero2.png')

    def display(self):
        '''
        把自己展示出来
        :return:
        '''
        self.window.blit(self.surface,(self.x,self.y))

    def moveLeft(self):
        self.x -= 1
    def moveRight(self):
        self.x += 1
    def moveUp(self):
        self.y -= 1
    def moveDown(self):
        self.y += 1
#初始化
pygame.init()

#加载背景
bg = pygame.image.load('img/img_bg_level_1.jpg')
#获取背景的高度宽度
bgW = bg.get_width()
bgH = bg.get_height()
#创建窗口
window = pygame.display.set_mode((bgW,bgH))
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
        elif event.type == KEYDOWN:
            if event.key == K_a:
                plane.moveLeft()
            if event.key == K_d:
                plane.moveRight()
            if event.key == K_w:
                plane.moveUp()
            if event.key == K_s:
                plane.moveDown()