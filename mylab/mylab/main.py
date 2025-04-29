# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QListWidget, QSplitter
from PyQt5.QtCore import Qt
from core.canvas import SimulationCanvas
from core.properties import PropertyPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BP Simulation Model")
        self.setGeometry(100, 100, 1400, 800)

        main_layout = QHBoxLayout()
        splitter = QSplitter(Qt.Horizontal)

        self.toolbox = QListWidget()
        self.toolbox.addItems(["BP Sensor", "Gain", "LowPassFilter", "HighPassFilter", "ADC", "Display"])

        self.property_panel = PropertyPanel()
        self.canvas = SimulationCanvas(self.property_panel)

        self.toolbox.itemDoubleClicked.connect(self.canvas.add_component)

        splitter.addWidget(self.toolbox)
        splitter.addWidget(self.canvas)
        splitter.addWidget(self.property_panel)

        container = QWidget()
        container.setLayout(main_layout)
        main_layout.addWidget(splitter)

        simulate_button = QPushButton("Run Simulation")
        simulate_button.clicked.connect(self.canvas.run_simulation)
        main_layout.addWidget(simulate_button)

        codegen_button = QPushButton("Generate C Code")
        codegen_button.clicked.connect(self.canvas.generate_c_code)
        main_layout.addWidget(codegen_button)

        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


