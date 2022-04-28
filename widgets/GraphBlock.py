from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QHBoxLayout, QVBoxLayout, QPushButton
from Chart import Chart

import numpy as np
import pyqtgraph as pg


class GraphBlock(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.chart_list = []

        self.addStretch()

    def add_chart(self):
        chart = Chart()
        self.chart_list.append(chart)
        self.addLayout(chart)
