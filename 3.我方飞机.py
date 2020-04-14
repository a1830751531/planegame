import pygame
from pygame.locals import *
import sys
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
hero = pygame.image.load('img/hero2.png')

while True:
    #展示在窗口
    window.blit(bg,(0,0))
    #展示飞机
    window.blit(hero,(200,600))
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