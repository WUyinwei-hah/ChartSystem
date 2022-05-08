"""
@Project: 软件构造课设
@Description: 包裹一个或多个chart组件的外窗体
@Time:2022/4/22
@Author:WYW

"""

from PyQt5.QtWidgets import QVBoxLayout
from Chart import Chart


class GraphBlock(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.addStretch()

    def add_chart(self, filename):
        """
        为被图块添加一个chart
        :param filename: 数据地址
        :return: 无
        """
        # 新增一个chart块
        chart = Chart(filename)
        self.addLayout(chart)



