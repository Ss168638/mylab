# === components/display.py ===
from .base import BaseComponent
import matplotlib.pyplot as plt

class Display(BaseComponent):
    def __init__(self):
        super().__init__("Display")
        self.params = {}

    def process(self, signal):
        if signal is not None:
            plt.plot(signal)
            plt.title("BP Output")
            plt.show()
        return signal
