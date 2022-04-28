"""'
@Project: 软件构造课设
@Description: 构造整个显示窗口的类
@Time:2022/4/22 19:45
@Author:MING

"""
import sys

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton
from HeaderBlock import HeaderBlock
from GraphBlock import GraphBlock


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 窗体属性
        self.setWindowTitle("Chart")
        self.resize(1080, 800)

        # 窗体位置, 调整居中
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 布局
        main_layout = QVBoxLayout()

        # header
        header_layout = HeaderBlock()
        main_layout.addLayout(header_layout)

        # 第一个chart
        self.graph_block = GraphBlock()
        main_layout.addLayout(self.graph_block)
        main_layout.addStretch()

        self.setLayout(main_layout)

        header_layout.add_chart_signal.connect(self.on_add_chart_signal)

    def on_add_chart_signal(self):
        self.graph_block.add_chart()
        print("add chart")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit((app.exec_()))
