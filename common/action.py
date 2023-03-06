import time

"""
手势操作
"""


def get_size(app):
    """获取屏幕宽高"""
    x = app.get_window_size()['width']
    y = app.get_window_size()['height']
    return x, y


def swipe_left(app):
    """模拟手指向左滑动<--"""
    size = get_size(app)
    start_x = int(size[0] * 0.9)
    start_y = int(size[1] * 0.5)
    end_x = int(size[0] * 0.1)
    end_y = int(size[1] * 0.5)
    app.swipe(start_x, start_y, end_x, end_y, 500)


def swipe_right(app):
    """模拟手指向右滑动-->"""
    size = get_size(app)
    start_x = int(size[0] * 0.1)
    start_y = int(size[1] * 0.5)
    end_x = int(size[0] * 0.9)
    end_y = int(size[1] * 0.5)
    app.swipe(start_x, start_y, end_x, end_y, 500)


def swipe_up(app):
    """模拟手指向上滑动"""
    size = get_size(app)
    start_x = int(size[0] * 0.5)
    start_y = int(size[1] * 0.65)
    end_x = int(size[0] * 0.5)
    end_y = int(size[1] * 0.35)
    app.swipe(start_x, start_y, end_x, end_y, 800)


def swipe_down(app):
    """模拟手指向下滑动"""
    size = get_size(app)
    start_x = int(size[0] * 0.5)
    start_y = int(size[1] * 0.35)
    end_x = int(size[0] * 0.5)
    end_y = int(size[1] * 0.65)
    app.swipe(start_x, start_y, end_x, end_y, 800)


def get_time():
    """获取时间"""
    return time.strftime("%Y-%m-%d %H:%M:%S")
