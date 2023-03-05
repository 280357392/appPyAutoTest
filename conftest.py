import os
import pytest
from datetime import datetime
from py.xml import html
from appium import webdriver
from appium.options.android import UiAutomator2Options

from config import RunConfig


def pytest_html_report_title(report):
    report.title = "APP UI自动化测试报告"


def pytest_configure(config):
    # 移除所有Environment项目。
    config._metadata = {}
    # 添加Environment项
    config._metadata["版本信息"] = "v1.0"
    config._metadata["APP名称信息"] = "短信APP"
    config._metadata["运行环境信息"] = "测试环境"


# @pytest.mark.optionalhook
@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试中心")])
    prefix.extend([html.p("测试人员: 蒙伟")])


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th("Description"))
    cells.insert(3, html.th("Time", class_="sortable time", col="time"))
    cells.pop()
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))  # Description
    cells.insert(3, html.td(datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'), class_="col-time"))  # Time
    cells.pop()
    cells.pop()


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的name和nodeid的中文显示在控制台上
    解决终端日志中文乱码
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
    extra = getattr(report, 'extra', [])
    # if report.when == 'call' or report.when == "setup":
    # 用例结束后才执行1次
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        # 失败时才截图
        # if (report.skipped and xfail) or (report.failed and not xfail):
        #     case_path = report.nodeid.replace("::", "_") + ".png"
        #     if "[" in case_path:
        #         case_name = case_path.split("-")[0] + "].png"
        #     else:
        #         case_name = case_path
        #     capture_screenshots(case_name)
        #     img_path = "image/" + case_name.split("/")[-1]
        #     if img_path:
        #         html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
        #                'onclick="window.open(this.src)" align="right"/></div>' % img_path
        #         extra.append(pytest_html.extras.html(html))

        # 无论是否失败都截图
        case_path = report.nodeid.replace("::", "_") + ".png"
        if "[" in case_path:
            case_name = case_path.split("-")[0] + "].png"
        else:
            case_name = case_path
        capture_screenshots(case_name)
        img_path = "image" + os.sep + case_name.split("/")[-1]
        if img_path:
            html = '<div><img src="%s" ' \
                   'alt="screenshot" style="border: 1px solid #e6e6e6;width:304px;height:240px;margin-left:5px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % img_path
            extra.append(pytest_html.extras.html(html))
    report.extra = extra
    # 再把编码改回来
    # 解决报告中文乱码问题
    report.nodeid = report.nodeid.encode("unicode_escape").decode("utf-8")


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]
    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    """
    global driver
    file_name = case_name.split(os.sep)[-1]
    if RunConfig.new_report is None:
        raise NameError('没有初始化测试报告目录')
    else:
        image_dir = os.path.join(RunConfig.new_report, "image", file_name)
        RunConfig.driver.save_screenshot(image_dir)


@pytest.fixture(scope='session', autouse=True)
def app():
    """
    启动app
    """
    global driver

    if RunConfig.driver_type == "android":
        # android
        options = UiAutomator2Options()
        options.platformVersion = '11'
        options.app_package = 'com.android.mms'
        options.app_activity = '.ui.MmsTabActivity'
        options.no_reset = True
        driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
        # driver = webdriver.Remote('http://localhost:4723/wd/hub', RunConfig.androidInfo)
        # driver.implicitly_wait(10)
    elif RunConfig.driver_type == "ios":
        # ios
        raise NameError("driver驱动类型定义错误！")
    else:
        # 其他
        raise NameError("driver驱动类型定义错误！")
    RunConfig.driver = driver
    return driver


@pytest.fixture(scope="session", autouse=True)
def app_close():
    """
    关闭app
    """
    yield driver
    driver.quit()


if __name__ == "__main__":
    capture_screenshots("test_dir/test_baidu_search.test_search_python.png")
