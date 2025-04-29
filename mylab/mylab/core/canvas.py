# === core/canvas.py ===
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt
from components import COMPONENT_MAP
from codegen.generator import generate_c_code

class SimulationCanvas(QGraphicsView):
    def __init__(self, property_panel):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.property_panel = property_panel
        self.components = []

    def add_component(self, item):
        name = item.text()
        if name in COMPONENT_MAP:
            component = COMPONENT_MAP[name]()
            component.setPos(100, 100)
            self.scene.addItem(component)
            self.components.append(component)

    def run_simulation(self):
        signal = None
        for component in self.components:
            signal = component.process(signal)
        print("Simulated Output (first 10):", signal[:10] if signal is not None else "No output")

    def generate_c_code(self):
        code = generate_c_code(self.components)
        with open("generated_bp_model.c", "w") as f:
            f.write(code)
        print("C code generated in generated_bp_model.c")

