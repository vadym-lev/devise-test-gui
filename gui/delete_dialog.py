from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QMessageBox
from gui.api_client import delete_test_result


class DeleteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Delete Test Result")
        self.layout = QVBoxLayout(self)

        self.record_id_input = QLineEdit()
        self.record_id_input.setPlaceholderText("Record ID")
        self.layout.addWidget(QLabel("Record ID:"))
        self.layout.addWidget(self.record_id_input)

        self.button_layout = QHBoxLayout()
        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_record)
        self.button_layout.addWidget(self.delete_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout.addWidget(self.cancel_button)

        self.layout.addLayout(self.button_layout)

    def delete_record(self):
        record_id = self.record_id_input.text()

        if not record_id:
            QMessageBox.warning(self, "Error", "Record ID is required")
            return

        try:
            record_id = int(record_id)
            delete_test_result(record_id)
            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Error", "Record ID must be an integer")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))