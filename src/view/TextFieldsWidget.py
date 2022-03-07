from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QSizePolicy, QTextEdit
from PyQt5.QtCore import Qt, pyqtSignal
from src.utils.Translator import Translator

tr = Translator.inst()


class TextFieldsWidget(QWidget):
    text_signal = pyqtSignal(str)

    def __init__(self):
        QWidget.__init__(self)

        self.setStyleSheet('background-color: white')
        self.__grid_layout = QGridLayout(self)
        self.__grid_layout.setSpacing(10)
        self.__grid_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.__grid_layout)

        self.__element_list = []
        self.__counter = 1

        self.add_line()

    def update_language(self):
        pass

    def update_element_position(self):
        element_number = 0
        for element in self.__element_list:
            self.__grid_layout.addWidget(element[0], element_number * 2, 0, 2, 5)
            self.__grid_layout.addWidget(element[1], element_number * 2, 5, 1, 1, Qt.AlignVCenter)
            self.__grid_layout.addWidget(element[2], element_number * 2 + 1, 5, 1, 1, Qt.AlignVCenter)
            element_number = element_number + 1

    def add_line(self):
        text_edit = QTextEdit('  ' + tr.text() + ' ' + str(self.__counter), self)
        text_edit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        close_button = QPushButton('X', self)
        close_button.setMaximumWidth(40)

        ok_button = QPushButton('OK', self)
        ok_button.setMaximumWidth(40)
        ok_button.pressed.connect(lambda: self.text_signal.emit(text_edit.toPlainText()))

        element = (text_edit, close_button, ok_button)
        self.__element_list.append(element)
        close_button.pressed.connect(lambda: self.close(element))

        self.update_element_position()
        self.__counter = self.__counter + 1

    def clear_text_fields(self):
        for element in self.__element_list:
            element[0].clear()

    def close(self, element: tuple):
        if element in self.__element_list:
            element[0].close()
            element[1].close()
            element[2].close()
            self.__grid_layout.removeWidget(element[0])
            self.__grid_layout.removeWidget(element[1])
            self.__grid_layout.removeWidget(element[2])
            self.__element_list.remove(element)
            self.update_element_position()
