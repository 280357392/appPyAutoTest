from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from page.base_page import BasePage
from page.home.new_mms_page import NewMmsPage


class HomePage(BasePage):
    """
    首页：
    """

    __mms_add_btn_by = (AppiumBy.ID, 'fab')
    '''新增+短信按钮 '''

    __mms_list_item1_by = (AppiumBy.XPATH,
                           '//*[@resource-id="android:id/list"]/android.view.ViewGroup[1]/*[@resource-id="com.android.mms:id/subject"]')
    '''第一条短信草稿，控件'''
    __toast = (AppiumBy.XPATH, '/hierarchy/android.widget.Toast')

    def __init__(self, app):
        super().__init__(app)

    def add_mms_draft(self, text):
        """
        新增短信草稿
        实例对象
        对象 = 对象.业务
        :param text: 短信内容。
        :return:
        """
        self.go_to_home(loc=self.__mms_add_btn_by)  # 回到指定页面
        self.find_element(self.__mms_add_btn_by).click()
        NewMmsPage(self.app).edit_mms(text)
        return self

    def get_list_item1_text(self):
        """
        获取列表第一条数据。
        新增的草稿由于延迟显示，所以获取的第一条数据可能是旧数据。
        为了避免这个问题需要加入强制等待。
        """
        sleep(2)
        return self.find_element(self.__mms_list_item1_by).text

    def get_toast_text(self):
        """
        获取toast信息。
        toast消失很快，所以需要马上获取。
        """
        return self.find_element(self.__toast).text
