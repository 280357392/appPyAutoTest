import os
import time
import logging
import pytest
import click
from config import RunConfig
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def mkdir_new_report(new_report, report_rootpath):
    """
    最新的测试报告为：new_report
    旧的测试报告为：report_rootpath/now_time
    """

    # 如果目录存在，先重命名目录
    if os.path.exists(new_report):
        now_time = ''
        files = os.listdir(new_report)
        for i in files:
            if 'html' in i:
                index = i.rfind('.')
                now_time = i[:index]
        if now_time == '':
            return
        os.rename(new_report, report_rootpath / now_time)
    os.mkdir(new_report)
    os.mkdir(Path(new_report) / 'image')


@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        logger.info("回归模式，开始执行✈✈！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        report_rootpath = Path.cwd() / 'report'
        new_report = str(report_rootpath / 'new_report')
        RunConfig.new_report = new_report
        mkdir_new_report(new_report, report_rootpath)
        html_report = os.path.join(new_report, "{}.html".format(now_time))
        pytest.main(["-v", RunConfig.case_path,  # 测试用例目录。
                     "--html=" + html_report,  # 测试报告文件路径。
                     "--self-contained-html",  # 合并css到html文件中。
                     "--maxfail", RunConfig.max_fail,  # 失败N次后停止测试。
                     "--reruns", RunConfig.rerun,  # 重试次数。
                     ])
        logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        # 不会产生报告
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", RunConfig.case_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()

'''
回归模式（生成报告）:
 $ python run_tests.py

调试模式（不生成报告）:
 $ python run_tests.py -m debug
'''
