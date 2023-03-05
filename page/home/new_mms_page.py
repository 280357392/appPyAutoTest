from appium.webdriver.common.appiumby import AppiumBy

from page.base_page import BasePage


class NewMmsPage(BasePage):
    """
    新增短信页
    """
    __recipient_input_by = (AppiumBy.ID, 'com.android.mms:id/recipients_viewer')
    '''收信人，输入框'''

    __recent_contacts_by = (
        AppiumBy.XPATH, '//*[@resource-id="com.android.mms:id/recent_contact_grid"]/android.widget.TextView[1]')
    '''最近联系人，控件'''

    # com.android.mms:id/embedded_text_editor
    __mms_input_by = (AppiumBy.ID, 'embedded_text_editor')
    '''短信内容，输入框'''

    __up_btn_by = (AppiumBy.ID, 'up')
    '''新增+短信按钮 '''

    def __init__(self, app):
        super().__init__(app)

    def edit_mms(self, text):
        """
        1、点击收信人输入框。\n
        2、选择第一个最近联系人。\n
        3、短信内容输入框中输入内容。\n
        4、返回上一页。\n
        :param text: 短信内容。
        :return:
        """
        self.find_element(self.__recipient_input_by).click()
        self.find_element(self.__recent_contacts_by).click()
        self.find_element(self.__mms_input_by).send_keys(text)
        self.find_element(self.__up_btn_by).click()
