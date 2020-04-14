import pygame
from pygame.locals import *
import sys
#初始化
pygame.init()
#创建窗口
window = pygame.display.set_mode((600,600))
#图标和标题
pygame.display.set_caption('飞机大战')
#图标
icon = pygame.image.load('img/app.ico')
pygame.display.set_icon(icon)

while True:
    #退出事件
    eventList = pygame.event.get()
    #遍历事件
    for event in eventList:
        if event.type == QUIT:
            #退出游戏
            pygame.quit()
            #退出程序
            sys.exit()