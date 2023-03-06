from appium.webdriver.common.appiumby import AppiumBy

from page.base_page import BasePage


class ExperimentPage(BasePage):
    """用于调试"""

    __menu_mine = (AppiumBy.XPATH, "//*[@resource-id='com.by.ferrari:id/menu_mine']")
    __mine_creation = (AppiumBy.XPATH, "//*[@resource-id='com.by.ferrari:id/mine_creation']")

    def __init__(self, app):
        super().__init__(app)

    def show_my_creation(self):
        self.find_element(self.__menu_mine).click()
        self.find_element(self.__mine_creation).click()
