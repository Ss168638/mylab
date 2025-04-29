# === core/properties.py ===
from PyQt6.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit

class PropertyPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.form = QFormLayout()
        self.setLayout(self.form)
        self.inputs = {}

    def show_properties(self, component):
        for i in reversed(range(self.form.count())):
            self.form.itemAt(i).widget().setParent(None)
        self.inputs.clear()
        self.form.addRow(QLabel(f"{component.name} Properties"))
        for prop in component.params:
            field = QLineEdit(str(component.params[prop]))
            field.editingFinished.connect(lambda prop=prop, field=field: component.set_param(prop, field.text()))
            self.form.addRow(prop, field)

