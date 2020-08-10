
"""
超简单刷视频工具，利用滑屏
"""
from appium import webdriver
import time

def shua(appPackage,appActivity,times):
    desired_caps ={
        'platformName':'Android',
        'deviceName':'',
        'platformVersion':'10',
        # 'app':r'\iBiliPlayer-bili.apk',
        'appPackage':appPackage,
        'appActivity':appActivity,
        # 'realDevice':False,
        "recreateChromeDriverSessions":True,
        "noReset":True,
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    driver.implicitly_wait(10)

    for i in range(0,times):
        print(i)
        time.sleep(10) # 每10秒滑动一次
        driver.swipe(0, 1671,307, 522)

# 微视
shua('com.tencent.weishi','com.tencent.oscar.module.splash.SplashActivity',100)
# 快手急速版
shua('com.kuaishou.nebula','com.yxcorp.gifshow.HomeActivity',100)
# 火山极速版
shua('com.ss.android.ugc.livelite','com.ss.android.ugc.live.main.MainActivity',100)
