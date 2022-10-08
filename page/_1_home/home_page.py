from appium.webdriver.common.appiumby import AppiumBy
from page.page import Page
from page._1_home.new_mms_page import NewMmsPage


class HomePage(Page):
    """
    首页：
    """

    __mms_add_btn_by = (AppiumBy.ID, 'fab')
    '''新增+短信按钮 '''

    __mms_list_item1_by = (AppiumBy.XPATH,
                   '//*[@resource-id="android:id/list"]/android.view.ViewGroup[1]/*[@resource-id="com.android.mms:id/subject"]')
    '''第一条短信草稿，控件'''

    def __init__(self, app):
        super().__init__(app)

    def add_mms_draft(self, text):
        """
        进入首页
        1、点击新增按钮。\n
        2、新增短信草稿
        :param text: 短信内容。
        :return:
        """
        self.skip_home()
        self.find_element(self.__mms_add_btn_by).click()
        NewMmsPage(self.app).edit_mms(text)

    def get_list_item1_text(self):
        return self.find_element(self.__mms_list_item1_by).text