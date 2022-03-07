from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout, QFrame, QPushButton

from src.view.TableWidget import TableWidget
from src.view.TextFieldsWidget import TextFieldsWidget
from src.utils.Translator import Translator

tr = Translator.inst()


class CentralWidget(QFrame):
    style_panel_changed = pyqtSignal()
    table_changed = pyqtSignal()
    text_panel_changed = pyqtSignal()

    def __init__(self):
        QFrame.__init__(self)

        self.__grid_layout = QGridLayout(self)
        self.setLayout(self.__grid_layout)
        self.__grid_layout.setSpacing(10)

        self.__style_panel_button = QPushButton(tr.hide_style_panel(), self)
        self.__style_panel_button.pressed.connect(lambda: self.style_panel_changed.emit())

        self.__table_button = QPushButton(tr.hide_table(), self)
        self.__table_button.pressed.connect(self.change_left_widget)

        self.__text_panel_button = QPushButton(tr.hide_text_panel(), self)
        self.__text_panel_button.pressed.connect(self.change_right_widget)

        self.__clear_text_fields_button = QPushButton(tr.clear_text_fields(), self)
        self.__add_text_field_button = QPushButton(tr.add_text_field(), self)

        self.__table_widget = TableWidget()
        self.text_fields_widget = TextFieldsWidget()

        self.__clear_text_fields_button.pressed.connect(self.text_fields_widget.clear_text_fields)
        self.__add_text_field_button.pressed.connect(self.text_fields_widget.add_line)

        self.__grid_layout.addWidget(self.__style_panel_button, 0, 0, 1, 2)
        self.__grid_layout.addWidget(self.__table_button, 0, 2, 1, 2)
        self.__grid_layout.addWidget(self.__text_panel_button, 0, 4, 1, 2)
        self.__grid_layout.addWidget(self.__clear_text_fields_button, 0, 6, 1, 2)
        self.__grid_layout.addWidget(self.__add_text_field_button, 0, 8, 1, 2)

        self.update_position_with_right_panel()

    def update_language(self):
        self.__table_button.setText(tr.hide_table()
                                    if self.__table_widget.isVisible()
                                    else tr.show_table()
                                    )

        self.__text_panel_button.setText(tr.hide_text_panel()
                                         if self.text_fields_widget.isVisible()
                                         else tr.show_text_panel()
                                         )

        self.__clear_text_fields_button.setText(tr.clear_text_fields())
        self.__add_text_field_button.setText(tr.add_text_field())
        self.__table_widget.update_language()
        self.text_fields_widget.update_language()

    def update_position_with_right_panel(self):
        self.__grid_layout.removeWidget(self.__table_widget)
        self.__grid_layout.removeWidget(self.text_fields_widget)
        self.__grid_layout.addWidget(self.__table_widget, 1, 0, 15, 5)
        self.__grid_layout.addWidget(self.text_fields_widget, 1, 5, 15, 5)

    def update_position_without_right_panel(self):
        self.__grid_layout.removeWidget(self.__table_widget)
        self.__grid_layout.removeWidget(self.text_fields_widget)
        self.__grid_layout.addWidget(self.__table_widget, 1, 0, 15, 10)

    def set_style_panel_name(self, text: str):
        self.__style_panel_button.setText(text)

    def change_left_widget(self):
        if self.__table_widget.isHidden():
            self.__table_widget.show()
            self.__table_button.setText(tr.hide_table())
        else:
            self.__table_widget.hide()
            self.__table_button.setText(tr.show_table())

    def change_right_widget(self):
        if self.text_fields_widget.isHidden():
            self.update_position_with_right_panel()
            self.text_fields_widget.show()
            self.__text_panel_button.setText(tr.hide_text_panel())
        else:
            self.text_fields_widget.hide()
            self.update_position_without_right_panel()
            self.__text_panel_button.setText(tr.show_text_panel())
