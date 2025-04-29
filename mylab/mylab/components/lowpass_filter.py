# === components/lowpass_filter.py ===
from .base import BaseComponent

class LowPassFilter(BaseComponent):
    def __init__(self):
        super().__init__("LowPassFilter")
        self.params = {"cutoff": 0.1}

    def process(self, signal):
        if signal is None:
            return np.zeros(1000)
        kernel = np.ones(int(1/self.params["cutoff"])) / (1/self.params["cutoff"])
        return np.convolve(signal, kernel, mode='same')

