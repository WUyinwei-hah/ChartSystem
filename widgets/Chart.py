"""
@Project: 软件构造课设
@Description: chart组件
@Time:2022/4/22
@Author:WYW

"""

import os
import numpy as np
import pyqtgraph as pg

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QCheckBox, QFileDialog
from utils import MathUtils


class Chart(QVBoxLayout):
    def __init__(self, filename):
        """
        初始化本chart块
        :param filename:用于初始化的数据
        """
        super().__init__()

        self.lines = []
        self.initial_btn_and_checkbox()
        self.initial_chart(filename)

    def initial_btn_and_checkbox(self):
        """
        初始化按钮组件和多选框，并绑定时间
        :return: 无
        """

        ##############################
        # 定义头部选择框
        ##############################
        self.setting_layout = QHBoxLayout()
        self.add_compare_line_btn = QPushButton("添加一条比对曲线")
        self.show_min_check_box = QCheckBox("显示最小值")
        self.show_max_check_box = QCheckBox("显示最大值")
        self.show_diff_check_box = QCheckBox("显示变化曲线")

        ##############################
        # 绑定事件
        ##############################
        self.add_compare_line_btn.clicked.connect(self.add_compare_line)
        self.show_min_check_box.stateChanged.connect(lambda: self.min_line_manage(self.show_min_check_box))
        self.show_max_check_box.stateChanged.connect(lambda: self.max_line_manage(self.show_max_check_box))
        self.show_diff_check_box.stateChanged.connect(lambda: self.diff_line_manage(self.show_diff_check_box))

        ##############################
        # 添加视图
        ##############################
        self.add_compare_line_btn
        self.setting_layout.addWidget(self.add_compare_line_btn)
        self.setting_layout.addWidget(self.show_min_check_box)
        self.setting_layout.addWidget(self.show_max_check_box)
        self.setting_layout.addWidget(self.show_diff_check_box)
        self.setting_layout.addStretch()

        ##############################
        # 应用
        ##############################
        self.addStretch()
        self.addLayout(self.setting_layout)

    def initial_chart(self, filename):
        """
        初始化本chart的基础图
        :param filename: 数据来源的文件
        :return: 无
        """

        ###############################
        # 初始化基础widget
        ##############################
        self.chart_widget = pg.GraphicsLayoutWidget(None, show=True)
        # 设置widget大小
        self.chart_widget.resize(600, 300)
        self.addWidget(self.chart_widget)
        # 创建一个Plot画板，命名为文件名
        self.plot = self.chart_widget.addPlot(title=filename.split("/")[-1])
        # 加legend
        self.plot.addLegend()
        # 加入网格
        self.plot.showGrid(x=True, y=True, alpha=0.5)

        ##############################
        # 加入第一个line
        ##############################
        self.add_new_line(filename, True)

    def add_new_line(self, filename, initial=False):
        """
        为本chart添加条新的曲线
        :param filename: 曲线数据文件名
        :param initial: 是否是第一条曲线
        :return: 无
        """
        data = np.load(filename)

        # 如果是主曲线存储起来后续使用
        if initial:
            self.data = data

        # 创建画笔
        chartPen = pg.mkPen(color=self.get_color(), width=2)

        # 加入随机的点数据, 显示文件名
        self.lines.append(
            self.plot.plot(y=data, pen=chartPen, title=filename.split("/")[-1], name=filename.split("/")[-1]))

    def add_compare_line(self):
        """
        在本chart中增加一条曲线
        :return:
        """

        # 打开文件选择器
        filename, _ = QFileDialog.getOpenFileName(None, '选择图像', os.getcwd(), "*.npy")
        # 空值判断
        if str(filename).strip() != "":
            self.add_new_line(filename)

    def min_line_manage(self, checkbox):
        """
        为chart的基础曲线增加最小值曲线
        :param checkbox: 被点击的checkbox对象
        :return: 无
        """

        # 判断多选框的的状态
        if checkbox.isChecked():
            # 显示
            y_data = MathUtils.get_min_array(self.data)
            self.min_line = self.plot.plot(y=y_data, pen='g', name="最小值")
        else:
            self.plot.removeItem(self.min_line)

    def max_line_manage(self, checkbox):
        """
        为chart的基础曲线增加最大值曲线
        :param checkbox: 被点击的checkbox对象
        :return: 无
        """

        # 判断多选框的的状态
        if checkbox.isChecked():
            # 显示
            y_data = MathUtils.get_max_array(self.data)
            self.max_line = self.plot.plot(y=y_data, pen='r', name="最大值")
        else:
            self.plot.removeItem(self.max_line)

    def diff_line_manage(self, checkbox):
        """
        为chart的基础曲线增加差值曲线
        :param checkbox: 被点击的checkbox对象
        :return: 无
        """

        # 判断多选框的的状态
        if checkbox.isChecked():
            # 显示
            y_data = MathUtils.get_diff_array(self.data)
            self.diff_line = self.plot.plot(y=y_data, pen='b', name="变化曲线")
        else:
            self.plot.removeItem(self.diff_line)

    def get_color(self):
        """
        返回画笔的颜色
        :return: 一个新的颜色
        """

        # 被选颜色数组
        color_array = [(107, 200, 224), (129, 236, 236), (255, 234, 167), (255, 118, 117), (60, 99, 130)]

        return color_array[(len(self.lines) + 1) % len(color_array)]
