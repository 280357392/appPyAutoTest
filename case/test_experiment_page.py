import pytest
from appium.webdriver.webdriver import WebDriver
from time import sleep

from config import RunConfig
from page.experiment_page import ExperimentPage


@pytest.mark.skipif('test_experiment_page.py' in RunConfig.skip_module, reason="跳过的模块")
class TestExperimentPage:
    """实验模块"""

    @pytest.mark.skipif(RunConfig.debug, reason="debug模式跳过用例")
    def test_001(self, app: WebDriver):
        experiment = ExperimentPage(app)
        experiment.show_my_creation()
        sleep(5)
