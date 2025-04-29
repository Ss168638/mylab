# === components/base.py ===
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter, Qt
import numpy as np

class BaseComponent(QGraphicsItem):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.params = {}
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def boundingRect(self):
        return QRectF(0, 0, 100, 50)

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.lightGray)
        painter.drawRect(0, 0, 100, 50)
        painter.drawText(10, 25, self.name)

    def set_param(self, key, value):
        self.params[key] = float(value)

    def process(self, signal):
        raise NotImplementedError

