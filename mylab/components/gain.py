# === components/gain.py ===
from .base import BaseComponent
import numpy as np

class Gain(BaseComponent):
    def __init__(self):
        super().__init__("Gain")
        self.params = {"gain": 2.0}

    def process(self, signal):
        if signal is None:
            signal = np.ones(1000)
        return signal * self.params["gain"]

