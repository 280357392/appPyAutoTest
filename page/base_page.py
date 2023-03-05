from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from time import sleep


class BasePage(object):

    def __init__(self, app: WebDriver):
        self.app = app

    def find_element(self, loc, timeout=5):
        """
        获取页面某个元素的对象。\n
        :param loc: 元组，如：(AppiumBy.ID, u"kw")
        :param timeout: 查找元素显式等待时间秒，如：1
        :return: 元素对象
        """
        message = '未查找到该元素，by：{}，value：{}'.format(*loc)
        return WebDriverWait(self.app, timeout=timeout).until(lambda d: d.find_element(*loc), message)

    def find_elements(self, loc, timeout=5):
        """
        获取页面元素
        :param loc: 元组，如(AppiumBy.ID, "id")
        :param timeout: 显示等待时间
        :return: 元素对象列表
        """
        message = '未查找到该元素组，by：{}，value：{}'.format(*loc)
        return WebDriverWait(self.app, timeout=timeout).until(lambda d: d.find_elements(*loc), message)

    def is_not_element(self, loc, timeout=5):
        """
        用于判断是否还能查找到被删除(隐藏)的元素。\n
        如果查找到元素，会报错。\n
        :param loc: 元组，如：(AppiumBy.ID, u"kw")
        :param timeout: 查找元素显式等待时间秒，如：1
        :return: 如果未找到元素时返回True，如果找到元素时报错。
        """
        message = '因为该元素被删除或者隐藏了，所以该元素不应存在，by：{}，value：{}'.format(*loc)
        return WebDriverWait(self.app, timeout=timeout).until_not(lambda d: d.find_element(*loc), message)

    def go_to_home(self, loc=(AppiumBy.ID, 'fab')):
        """
        回到首页
        """
        i = 0
        index = True
        while index and i < 20:
            sleep(0.2)
            try:
                # 是否是首页(检测首页标志性的控件)
                self.find_element(loc, timeout=1)
            except TimeoutException:
                # 出错时执行的代码块。
                self.app.back()
                i += 1
            else:
                # 没有出错时执行的代码块。
                index = False
