import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication, QHBoxLayout, QVBoxLayout, QPushButton


class HeaderBlock(QHBoxLayout):
    # 定义信号
    add_chart_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

        # 定义头部按钮并绑定槽函数
        add_graph_block_btn = QPushButton("添加图块")
        add_graph_block_btn.clicked.connect(self.add_graph_block)

        reset_btn = QPushButton("重置所有图块")
        reset_btn.clicked.connect(self.reset)

        # 添加按钮
        self.addWidget(add_graph_block_btn)
        self.addWidget(reset_btn)
        self.addStretch()



    def add_graph_block(self):
        filename = QFileDialog.getOpenFileName(None, '选择图像', os.getcwd())
        # TODO: 选择完成后选择是加在现有的还是新开一个block
        self.add_chart_signal.emit()

    def reset(self):
        print("reset")
