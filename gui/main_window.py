import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QLineEdit, QHBoxLayout, QDialog, QMessageBox
from gui.api_client import get_statistics
from gui.add_dialog import AddDialog
from gui.delete_dialog import DeleteDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Test Results")
        self.setGeometry(100, 100, 1000, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.filter_layout = QHBoxLayout()

        self.sensor_type_input = QLineEdit()
        self.sensor_type_input.setPlaceholderText("Sensor Type")
        self.filter_layout.addWidget(self.sensor_type_input)

        self.operator_input = QLineEdit()
        self.operator_input.setPlaceholderText("Operator")
        self.filter_layout.addWidget(self.operator_input)

        self.start_date_input = QLineEdit()
        self.start_date_input.setPlaceholderText("Start Date (YYYY-MM-DD)")
        self.filter_layout.addWidget(self.start_date_input)

        self.end_date_input = QLineEdit()
        self.end_date_input.setPlaceholderText("End Date (YYYY-MM-DD)")
        self.filter_layout.addWidget(self.end_date_input)

        self.filter_button = QPushButton("Filter")
        self.filter_button.clicked.connect(self.load_data)
        self.filter_layout.addWidget(self.filter_button)

        self.layout.addLayout(self.filter_layout)

        self.add_button = QPushButton("Add Test Result")
        self.add_button.clicked.connect(self.show_add_dialog)
        self.layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete Test Result")
        self.delete_button.clicked.connect(self.show_delete_dialog)
        self.layout.addWidget(self.delete_button)

        self.load_data()

    def load_data(self):
        sensor_type = self.sensor_type_input.text()
        operator = self.operator_input.text()
        start_date = self.start_date_input.text()
        end_date = self.end_date_input.text()

        try:
            data = get_statistics(sensor_type, operator, start_date, end_date)
            self.table.setRowCount(0)
            self.table.setColumnCount(4)
            self.table.setHorizontalHeaderLabels(
                ["Sensor Type", "Total Tests", "Successful Tests", "Unsuccessful Tests"])
            for row_data in data:
                row_number = self.table.rowCount()
                self.table.insertRow(row_number)
                self.table.setItem(row_number, 0, QTableWidgetItem(row_data["sensor_type"]))
                self.table.setItem(row_number, 1, QTableWidgetItem(str(row_data["total_tests"])))
                self.table.setItem(row_number, 2, QTableWidgetItem(str(row_data["successful_tests"])))
                self.table.setItem(row_number, 3, QTableWidgetItem(str(row_data["unsuccessful_tests"])))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def show_add_dialog(self):
        dialog = AddDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.load_data()

    def show_delete_dialog(self):
        dialog = DeleteDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.load_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    