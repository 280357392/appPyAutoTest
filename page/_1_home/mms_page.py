from appium.webdriver.common.appiumby import AppiumBy
from page.page import Page


class MmsPage(Page):
    """
    短信首页：
    """

    mms_add_btn_by = (AppiumBy.ID, 'fab')
    '''新增短信按钮 '''

    recipient_input_by = (AppiumBy.ID, 'com.android.mms:id/recipients_viewer')
    '''收信人输入框'''

    recent_contacts_by = (
        AppiumBy.XPATH, '//*[@resource-id="com.android.mms:id/recent_contact_grid"]/android.widget.TextView[1]')
    '''最近联系人'''

    mms_input_by = (AppiumBy.ID, 'embedded_text_editor')
    '''短信内容输入框'''

    def __init__(self, app):
        super().__init__(app)

    def add_mms(self, text):
        """
        1、点击新增按钮。\n
        2、点击收信人输入框。\n
        3、选择第一个最近联系人。\n
        4、短信内容输入框中输入内容。\n
        :param text: 短信内容。
        :return:
        """
        self.find_element(self.mms_add_btn_by).click()
        self.find_element(self.recipient_input_by).click()
        self.find_element(self.recent_contacts_by).click()
        self.find_element(self.mms_input_by).send_keys(text)

