# coding=utf-8

from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Mi6',
    'platformVersion': '8.0.0',
    #apk包名
    'appPackage': 'com.etnet.android.iq',
    #apk的launcherActivity
    'appActivity': '.MainActivity'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 休眠三秒等待页面加载完成

time.sleep(3)
driver.find_element_by_id("com.etnet.android.iq:id/close_btn").click()

# 获取当前界面activity
# ac = driver.current_activity
# print(ac)


# # 等广告页面activity出现,30秒内
# driver.wait_activity("com.google.android.gms.ads.AdActivity", 30)

# #关闭广告
# driver.find_element_by_class_name("android.widget.ImageButton").click()

#获取当前页面所有元素
# el = driver.find_elements_by_class_name('android.view.View(text)')
# # print(el)
# print "list1[0]: ", el

#获得机器屏幕大小x,y
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)

def swipeUp(t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5     # x坐标
    y1 = l['height'] * 0.75   # 起始y坐标
    y2 = l['height'] * 0.25   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(t=500, n=1):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5          # x坐标
    y1 = l['height'] * 0.25        # 起始y坐标
    y2 = l['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)

def swipLeft(t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

def swipRight(t=500, n=1):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

swipeUp(1000, 5)
