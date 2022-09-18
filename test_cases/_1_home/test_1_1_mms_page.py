import pytest
from config import RunConfig
from page._1_home.mms_page import MmsPage


# 方法执行顺序：谁先定义谁先执行。
# 用例之间不应相互依赖。
@pytest.mark.skipif('_1_home' in RunConfig.skip_module, reason="跳过的模块")
@pytest.mark.run(order=1)
class TestMmsPage:
    """短信操作"""

    @pytest.mark.skipif(RunConfig.debug, reason="debug模式跳过用例")
    def test_add_mms(self, app):
        """
        用例名称：新增一条短信，存为草稿。
        """
        # 回到首页
        page = MmsPage(app)
        page.skip_home(page.mms_add_btn_by)
        page.add_mms('自动化测试咯！！！')
        # assert
        page.skip_home(page.mms_add_btn_by)


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_mms.py"])
