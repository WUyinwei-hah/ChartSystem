from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton, QGroupBox, \
    QCheckBox
import numpy as np
import pyqtgraph as pg


class Chart(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.setting_layout = QHBoxLayout()

        box_group = QGroupBox("显示设置")
        box_group.setFlat(False)

        # 定义头部选择框
        self.add_compare_line_btn = QPushButton("添加一条比对曲线")
        # self.add_compare_line_btn.stateChanged.connect()
        self.show_min_check_box = QCheckBox("显示最小值")
        self.show_max_check_box = QCheckBox("显示最大值")
        self.show_diff_check_box = QCheckBox("显示变化曲线")

        self.setting_layout.addWidget(self.add_compare_line_btn)
        self.setting_layout.addWidget(self.show_min_check_box)
        self.setting_layout.addWidget(self.show_max_check_box)
        self.setting_layout.addWidget(self.show_diff_check_box)
        self.setting_layout.addStretch()

        self.addStretch()
        self.addLayout(self.setting_layout)

        win = pg.GraphicsLayoutWidget(None, show=True)
        # 设置widget大小
        win.resize(600, 300)
        # 创建画笔
        chartPen1 = pg.mkPen(color=(107, 200, 224), width=3)
        # 创建一个Plot画板
        plot = win.addPlot(title="随机数据对比")
        # 加入随机的点数据
        plot.plot(y=np.random.normal(size=30), pen=chartPen1, title="随机数据1")

        # 创建画笔
        chartPen2 = pg.mkPen(color=(192, 80, 77), width=3)
        plot.plot(y=np.random.normal(size=30) + 5, pen=chartPen2, title="随机数据2", symbolPen='w')

        self.addWidget(win)
