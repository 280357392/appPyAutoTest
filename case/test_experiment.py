import pytest
from appium.webdriver.webdriver import WebDriver

from config import RunConfig
from page.experiment_page import ExperimentPage


@pytest.mark.skipif('test_experiment.py' in RunConfig.skip_module, reason="跳过的模块")
class TestExperiment:
    """实验模块"""

    @pytest.mark.skipif(RunConfig.debug, reason="debug模式跳过用例")
    def test_001(self, app: WebDriver):
        experiment_page = ExperimentPage(app)
        experiment_page.test()

