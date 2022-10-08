import pytest
from config import RunConfig
from page._1_home.home_page import HomePage


# 方法执行顺序：谁先定义谁先执行。
# 用例之间不应相互依赖。
@pytest.mark.skipif('_1_home' in RunConfig.skip_module, reason="跳过的模块")
@pytest.mark.run(order=1)
class TestMmsPage:
    """短信操作"""

    # @pytest.mark.skipif(RunConfig.debug, reason="debug模式跳过用例")
    def test_add_mms(self, app):
        """
        用例名称：新增一条短信，存为草稿。
        """
        # 回到首页
        page = HomePage(app)
        page.add_mms_draft('自动化测试咯！！！')
        assert page.get_list_item1_text() == '自动化测试咯！！！'

