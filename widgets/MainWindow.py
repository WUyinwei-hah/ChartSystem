"""
@Project: 软件构造课设
@Description: 构造整个显示窗口的类
@Time:2022/4/22
@Author:WYW

"""
import sys

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QApplication
from HeaderBlock import HeaderBlock
from GraphBlock import GraphBlock


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initial_main_window()

    def initial_main_window(self):
        #####################################
        # 窗体属性
        #####################################

        # 窗体大小和title
        self.setWindowTitle("Chart")
        self.resize(1080, 800)
        # 窗体位置, 调整居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        #####################################
        # 总体布局初始化
        #####################################
        self.main_layout = QVBoxLayout()
        self.initial_header()
        self.initial_graph_block()

        #####################################
        # 应用总布局
        #####################################
        self.setLayout(self.main_layout)

    def initial_header(self):
        """
        初始化头部组件
        :return: 无
        """
        header_layout = HeaderBlock()
        header_layout.add_chart_signal.connect(self.on_add_chart_signal)
        self.main_layout.addLayout(header_layout)

    def initial_graph_block(self):
        """
        初始化图像组件
        :return: 无
        """

        self.graph_block = GraphBlock()
        self.main_layout.addLayout(self.graph_block)
        self.main_layout.addStretch()

    def on_add_chart_signal(self, filename):
        """
        用于监听来自于 header_layout 的按钮事件
        :param filename: 存储数据的文件夹的名字
        :return: 无
        """
        self.graph_block.add_chart(filename)


if __name__ == '__main__':
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
