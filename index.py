# coding=utf-8

from appium import webdriver
import time
desired_caps = {
                'platformName': 'Android',
                'deviceName': 'b6775e4d',
                'platformVersion': '8.0.0',

                # apk包名

                'appPackage': 'com.etnet.android.iq',

                # apk的launcherActivity

                'appActivity': '.MainActivity'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 休眠三秒等待页面加载完成

time.sleep(3)
driver.find_element_by_id("com.etnet.android.iq:id/close_btn").click()
