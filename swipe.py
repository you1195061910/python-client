#!/usr/bin/env python
#coding=utf-8
import os
PATH = lambda p: os.path.abspath(p)
SCREEN_PATH = PATH(os.path.join(os.getcwd(), "./screen"))

class Swipe(object):
    def __init__(self, driver):
        self.driver = driver
        
    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5     # x坐标
        y1 = l['height'] * 0.75   # 起始y坐标
        y2 = l['height'] * 0.25   # 终点y坐标
        for i in range(n):
            fileName = PATH(SCREEN_PATH + "/element" + bytes(i) + ".png")     
            self.driver.save_screenshot(fileName)
            self.driver.swipe(x1, y1, x1, y2, t)
            box = (x1, y1, x1, y2)
            print box


    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5          # x坐标
        y1 = l['height'] * 0.25        # 起始y坐标
        y2 = l['height'] * 0.75         # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2,t)

    def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)