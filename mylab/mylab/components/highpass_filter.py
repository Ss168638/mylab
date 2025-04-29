# === components/highpass_filter.py ===
from .base import BaseComponent
from scipy.signal import butter, filtfilt

class HighPassFilter(BaseComponent):
    def __init__(self):
        super().__init__("HighPassFilter")
        self.params = {"cutoff": 0.1}

    def process(self, signal):
        if signal is None:
            return np.zeros(1000)
        b, a = butter(1, self.params["cutoff"], btype='high', analog=False)
        return filtfilt(b, a, signal)
