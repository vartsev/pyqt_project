from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem
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
        id_width = 50
        value_width = 100
        self.__delta_width = id_width + value_width + 3
        self.__table.horizontalHeader().resizeSection(0, id_width)
        self.__table.horizontalHeader().resizeSection(3, value_width)

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

    def resizeEvent(self, event: QResizeEvent) -> None:
        QWidget.resizeEvent(self, event)
        self.__table.horizontalHeader().resizeSection(1, self.__table.width() - self.__delta_width)

    def add_line(self):
        self.__table.insertRow(self.__table.rowCount())
        for column in range(3):
            text = str(self.__table.rowCount())
            if column == 0:
                self.__table.setItem(self.__table.rowCount() - 1, column, QTableWidgetItem('Id_' + text))
            elif column == 1:
                self.__table.setItem(self.__table.rowCount() - 1, column, QTableWidgetItem(tr.parameter() + '_' + text))
            elif column == 2:
                self.__table.setItem(self.__table.rowCount() - 1, column, QTableWidgetItem(text + text + text))

    def delete_line(self):
        self.__table.removeRow(self.__table.rowCount() - 1)
