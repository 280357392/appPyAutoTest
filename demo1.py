from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from config import RunConfig
from time import sleep

driver = webdriver.Remote('http://localhost:4723/wd/hub', RunConfig.androidInfo)
driver.implicitly_wait(10)





driver.back()
sleep(2)
driver.quit()
