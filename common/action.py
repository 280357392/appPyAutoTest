import time

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

"""
手势操作
"""


def get_size(app):
    """获取屏幕宽高"""
    x = app.get_window_size()['width']
    y = app.get_window_size()['height']
    return x, y


def swipe_left(app, duration=500, n=1):
    """
    模拟手指向左滑动<--

    执行该操作前需确保页面可滑动，通常会sleep(2)一定时间。
    """
    size = get_size(app)
    start_x = int(size[0] * 0.9)
    start_y = int(size[1] * 0.5)
    end_x = int(size[0] * 0.1)
    end_y = int(size[1] * 0.5)
    for _ in range(n):
        app.swipe(start_x, start_y, end_x, end_y, duration)


def swipe_right(app, duration=500, n=1):
    """
    模拟手指向右滑动-->

    执行该操作前需确保页面可滑动，通常会sleep(2)一定时间。
    """
    size = get_size(app)
    start_x = int(size[0] * 0.1)
    start_y = int(size[1] * 0.5)
    end_x = int(size[0] * 0.9)
    end_y = int(size[1] * 0.5)
    for _ in range(n):
        app.swipe(start_x, start_y, end_x, end_y, duration)


def swipe_up(app, duration=800, n=1):
    """
    模拟手指向上滑动。

    执行该操作前需确保页面可滑动，通常会sleep(2)一定时间。
    """
    size = get_size(app)
    start_x = int(size[0] * 0.5)
    start_y = int(size[1] * 0.65)
    end_x = int(size[0] * 0.5)
    end_y = int(size[1] * 0.35)
    for _ in range(n):
        app.swipe(start_x, start_y, end_x, end_y, duration)


def swipe_down(app, duration=800, n=1):
    """
    模拟手指向下滑动。

    执行该操作前需确保页面可滑动，通常会sleep(2)一定时间。
    """
    size = get_size(app)
    start_x = int(size[0] * 0.5)
    start_y = int(size[1] * 0.35)
    end_x = int(size[0] * 0.5)
    end_y = int(size[1] * 0.65)
    for _ in range(n):
        app.swipe(start_x, start_y, end_x, end_y, duration)


def pinch(app):
    """缩小操作(弃用)"""
    size = get_size(app)
    action1 = TouchAction(app)
    action2 = TouchAction(app)
    action1.press(x=size[0] * 0.2, y=size[1] * 0.2).wait(1000).move_to(x=size[0] * 0.4, y=size[1] * 0.4).wait(
        1000).release()
    action2.press(x=size[0] * 0.8, y=size[1] * 0.8).wait(1000).move_to(x=size[0] * 0.6, y=size[1] * 0.6).wait(
        1000).release()
    pinch_action = MultiAction(app)
    pinch_action.add(action1, action2)
    pinch_action.perform()


def zoom(app):
    """放大操作(弃用)"""
    size = get_size(app)
    action1 = TouchAction(app)
    action2 = TouchAction(app)
    action1.press(x=size[0] * 0.4, y=size[1] * 0.4).wait(1000).move_to(x=size[0] * 0.2, y=size[1] * 0.2).wait(
        1000).release()
    action2.press(x=size[0] * 0.6, y=size[1] * 0.6).wait(1000).move_to(x=size[0] * 0.8, y=size[1] * 0.8).wait(
        1000).release()
    zoom_action = MultiAction(app)
    zoom_action.add(action1, action2)
    zoom_action.perform()


def get_time():
    """获取时间"""
    return time.strftime("%Y-%m-%d %H:%M:%S")
