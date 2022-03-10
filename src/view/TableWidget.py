from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem, QHeaderView
from src.utils.Translator import Translator

tr = Translator.inst()


class TableWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setStyleSheet('background-color: white')
        grid_layout = QGridLayout(self)
        grid_layout.setSpacing(10)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(grid_layout)

        self.__table = QTableWidget(self)
        self.__table.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.__table.setColumnCount(3)
        self.__table.setRowCount(0)
        self.__table.setHorizontalHeaderLabels(["Id", tr.parameter(), tr.value()])
        self.__table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.__table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.__table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)

        self.__table.verticalHeader().hide()
        grid_layout.addWidget(self.__table, 0, 0, 1, 2)

        self.__add_line_button = QPushButton(tr.add_line(), self)
        self.__add_line_button.pressed.connect(self.add_line)
        grid_layout.addWidget(self.__add_line_button, 1, 0, 1, 1)

        self.__delete_line_button = QPushButton(tr.del_line(), self)
        self.__delete_line_button.pressed.connect(self.delete_line)
        grid_layout.addWidget(self.__delete_line_button, 1, 1, 1, 1)

    def update_language(self):
        self.__table.setHorizontalHeaderLabels(["Id", tr.parameter(), tr.value()])
        self.__add_line_button.setText(tr.add_line())
        self.__delete_line_button.setText(tr.del_line())

    def add_line(self):
        row_index = self.__table.rowCount()
        self.__table.setRowCount(row_index + 1)

        self.__table.setItem(row_index, 0, QTableWidgetItem(f'Id_{row_index}'))
        self.__table.setItem(row_index, 1, QTableWidgetItem(tr.parameter() + str(row_index)))
        self.__table.setItem(row_index, 2, QTableWidgetItem(str(row_index) * 3))

    def delete_line(self):
        self.__table.removeRow(self.__table.rowCount() - 1)
