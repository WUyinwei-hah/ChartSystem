"""
@Project: 软件构造课设
@Description: 程序的头部按钮块
@Time:2022/4/22
@Author:WYW

"""

import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QPushButton


class HeaderBlock(QHBoxLayout):
    # 定义信号
    add_chart_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initial_btn()

    def initial_btn(self):
        #####################################
        # 定义头部按钮并绑定槽函数
        #####################################
        add_graph_block_btn = QPushButton("添加图块")
        add_graph_block_btn.clicked.connect(self.add_graph_block)

        #####################################
        # 添加按钮
        #####################################
        self.addWidget(add_graph_block_btn)
        self.addStretch()

    def add_graph_block(self):
        """
        新增图像模块按钮被按下后的槽函数，发出信号
        :return: 无
        """

        # 选择文件
        filename, _ = QFileDialog.getOpenFileName(None, '选择图像', os.getcwd(), "*.npy")
        # 空值判断
        if str(filename).strip() != "":
            self.add_chart_signal.emit(filename)
