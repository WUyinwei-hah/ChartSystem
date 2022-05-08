import sys

from PyQt5.QtWidgets import QApplication
from widgets.MainWindow import MainWindow


def run_application():
    """
    运行程序
    :return: 无
    """
    #####################################
    # 初始化软件
    #####################################
    app = QApplication(sys.argv)

    #####################################
    # 新建窗口并展示
    #####################################
    window = MainWindow()
    window.show()

    #####################################
    # 清除进程
    #####################################
    sys.exit((app.exec_()))


if __name__ == '__main__':
    run_application()
