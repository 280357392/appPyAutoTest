from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from config import RunConfig
from time import sleep

driver = webdriver.Remote('http://localhost:4723/wd/hub', RunConfig.androidInfo)
driver.implicitly_wait(10)

mms_list_by = (AppiumBy.XPATH,
                 '//*[@resource-id="android:id/list"]/android.view.ViewGroup[1]/*[@resource-id="com.android.mms:id/subject"]')
'''第一条短信草稿，控件'''
t = driver.find_element(*mms_list_by).text
print(t)


driver.back()
sleep(2)
driver.quit()
