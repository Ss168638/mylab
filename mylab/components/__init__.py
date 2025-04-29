# === components/__init__.py ===
from .gain import Gain
from .lowpass_filter import LowPassFilter
from .highpass_filter import HighPassFilter
from .adc import ADC
from .display import Display

COMPONENT_MAP = {
    "Gain": Gain,
    "LowPassFilter": LowPassFilter,
    "HighPassFilter": HighPassFilter,
    "ADC": ADC,
    "Display": Display,
}