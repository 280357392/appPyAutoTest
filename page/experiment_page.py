from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from page.base_page import BasePage


class ExperimentPage(BasePage):
    """用于调试"""

    __search_box_text = (AppiumBy.ID, "com.android.chrome:id/search_box_text")
    __url_bar = (AppiumBy.ID, "com.android.chrome:id/url_bar")
    __line_1 = (AppiumBy.ID, "com.android.chrome:id/line_1")
    __index_form = (AppiumBy.XPATH, '//*[@id="index-form"]')
    __index_kw = (AppiumBy.XPATH, '//*[@id="index-kw"]')
    __index_bn = (AppiumBy.XPATH, '//*[@id="index-bn"]')

    def __init__(self, app):
        super().__init__(app)

    def test(self):
        # search_box_text = self.find_element(self.__search_box_text)
        # search_box_text.click()
        url_bar = self.find_element(self.__url_bar)
        url_bar.click()
        url_bar.send_keys('https://www.baidu.com/')
        self.find_elements(self.__line_1)[0].click()

        # print(self.app.contexts)
        self.app.switch_to.context('WEBVIEW_chrome')

        # chrome://inspect/#devices
        self.find_element(self.__index_form).click()
        self.find_element(self.__index_kw).send_keys('美女')
        self.find_element(self.__index_bn).click()

        sleep(10)
