import pytest
from appium.webdriver.webdriver import WebDriver

from config import RunConfig
from page.home.home_page import HomePage


# 方法执行顺序：谁先定义谁先执行。
# 用例之间不应相互依赖。
@pytest.mark.skipif('test_home_page.py' in RunConfig.skip_module, reason="跳过的模块")
@pytest.mark.run(order=1)
class TestHomePage:
    """home模块"""

    @pytest.mark.skipif(RunConfig.debug, reason="debug模式跳过用例")
    def test_add_mms(self, app: WebDriver):
        """
        用例名称：新增一条短信，存为草稿。
        """
        home_page = HomePage(app)
        home_page = home_page.add_mms_draft('自动化测试咯')
        assert '信息已存为草稿。' == home_page.get_toast_text()  # 优先判断
        assert '自动化测试咯' == home_page.get_list_item1_text()

