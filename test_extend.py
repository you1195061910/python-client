#coding=utf-8

import unittest
import os
import time

from extend import Appium_Extend
from appium import webdriver
from swipe import Swipe

class Test(unittest.TestCase):
    #初始化环境
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Mi6',
            'platformVersion': '8.0.0',
            #apk包名
            'appPackage': 'com.etnet.android.iq',
            #apk的launcherActivity
            'appActivity': '.MainActivity'
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        self.extend = Appium_Extend(self.driver)

        #回到主屏幕
        # self.driver.press_keycode(3)
        self.swipe = Swipe(self.driver)

    def close_ad(self):
        time.sleep(3)
        close_btn = self.driver.find_element_by_id("com.etnet.android.iq:id/close_btn")
        if close_btn:
            close_btn.click()  
    #退出测试
    def tearDown(self):
        self.driver.quit()

    def test_get_screen_by_elements(self):
        self.close_ad()
        elements = self.driver.find_elements_by_class_name("android.view.View")
        self.extend.get_screenshot_by_elements(elements)

    def test_get_screen_by_custom(self):
        self.close_ad()
        time.sleep(3)
        scrollview = self.driver.find_element_by_id("com.etnet.android.iq:id/ScrollView")
           
        print(self.driver.get_window_rect())
        self.extend.get_screenshot_by_scroll(scrollview)
        element = self.driver.find_element_by_id("android:id/statusBarBackground")
        size = element.size

        # self.extend.get_screenshot_by_custom_size(0, size["height"], size["width"], 1920-60-160)
        self.swipe.swipeUp(1000, 4)
        # self.extend.get_screenshot_by_custom_size(0, size["height"], size["width"], 1920-60-160)

    def test_same_as(self):
        element = self.driver.find_elements_by_class_name("android.view.View")

        load = self.extend.load_image("f:\\screen\\image.png")
        #要求百分百相似
        result = self.extend.get_screenshot_by_element(element).same_as(load, 0)
        self.assertTrue(result)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(Test("setUp"))
    # suite.addTest(Test("close_ad"))
    suite.addTest(Test("test_get_screen_by_custom"))
    # suite.addTest(Test("test_same_as"))
    #执行测试
    unittest.TextTestRunner().run(suite)
