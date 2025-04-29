# === components/base.py ===
from PyQt6.QtWidgets import QGraphicsItem
from PyQt6.QtCore import QRectF, Qt
from PyQt6.QtGui import QPainter
import numpy as np

class BaseComponent(QGraphicsItem):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.params = {}
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

    def boundingRect(self):
        return QRectF(0, 0, 100, 50)

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.GlobalColor.lightGray)
        painter.drawRect(0, 0, 100, 50)
        painter.drawText(10, 25, self.name)

    def set_param(self, key, value):
        self.params[key] = float(value)

    def process(self, signal):
        raise NotImplementedError

