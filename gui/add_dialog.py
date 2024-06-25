from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QMessageBox
from gui.api_client import create_test_result


class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Test Result")
        self.layout = QVBoxLayout(self)

        self.sensor_type_input = QLineEdit()
        self.sensor_type_input.setPlaceholderText("Sensor Type")
        self.layout.addWidget(QLabel("Sensor Type:"))
        self.layout.addWidget(self.sensor_type_input)

        self.operator_input = QLineEdit()
        self.operator_input.setPlaceholderText("Operator")
        self.layout.addWidget(QLabel("Operator:"))
        self.layout.addWidget(self.operator_input)

        self.test_time_input = QLineEdit()
        self.test_time_input.setPlaceholderText("Test Time (YYYY-MM-DD HH:MM:SS)")
        self.layout.addWidget(QLabel("Test Time:"))
        self.layout.addWidget(self.test_time_input)

        self.success_input = QLineEdit()
        self.success_input.setPlaceholderText("Success (1 or 0)")
        self.layout.addWidget(QLabel("Success:"))
        self.layout.addWidget(self.success_input)

        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_record)
        self.button_layout.addWidget(self.add_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.button_layout)

    def add_record(self):
        sensor_type = self.sensor_type_input.text()
        operator = self.operator_input.text()
        test_time = self.test_time_input.text()
        success = self.success_input.text()

        if not (sensor_type and operator and test_time and success):
            QMessageBox.warning(self, "Error", "All fields are required")
            return

        try:
            success = int(success)
            test_result = {
                "sensor_type": sensor_type,
                "operator": operator,
                "date": test_time,
                "success": success
            }
            create_test_result(test_result)
            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Error", "Success must be an integer (1 or 0)")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

            