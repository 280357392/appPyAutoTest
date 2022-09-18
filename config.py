import os
from pathlib import Path


class RunConfig:
    """
    运行测试配置
    """
    debug = True
    """等于True时表示调试模式，将跳过全部用例。"""

    skip_module = [
        # '_1_home',
    ]
    """跳过的模块"""

    cases_path = str(Path.cwd() / 'test_cases')
    """测试用例目录"""

    new_report = ""
    """测试报告目录（默认test_report，此处配置无效）"""

    rerun = "0"
    """失败重跑次数"""

    max_fail = "5"
    """当达到最大失败数，停止执行"""

    driver_type = "android"

    driver = None
    """app默认驱动"""

    androidInfo = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "23121870",
        "appPackage": "com.android.mms",
        "appActivity": "com.android.mms.ui.MmsTabActivity",
        "noReset": True,
        "automationName": "uiautomator2",
        "unicodeKeyboard": True,
        "resetKeyboard": True,
    }
    """android设备info"""
