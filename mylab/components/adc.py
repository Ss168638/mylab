# === components/adc.py ===
from .base import BaseComponent
import numpy as np
class ADC(BaseComponent):
    def __init__(self):
        super().__init__("ADC")
        self.params = {"levels": 256}

    def process(self, signal):
        return np.round(signal * self.params["levels"]) / self.params["levels"] if signal is not None else None
