from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import pyqtSignal
from src.view.ListWidget import ListWidget
from src.utils.Translator import Translator

tr = Translator.inst()


class StyleWidget(QDockWidget):
    style_changed = pyqtSignal(str)

    def __init__(self, parent):
        QDockWidget.__init__(self, tr.style(), parent)

        self.__list_widget = ListWidget()
        self.setWidget(self.__list_widget)
        self.setFloating(False)
        self.setMaximumWidth(150)

        self.__style_map = {'Grey': 0, 'Red': 1, 'Green': 2, 'Blue': 3}
        self.__inverse_style_map = {v: k for k, v in self.__style_map.items()}
        self.__list_widget.currentItemChanged.connect\
            (
                lambda: self.style_changed.emit
                (
                    self.__inverse_style_map[self.__list_widget.row(self.__list_widget.currentItem())]
                )
            )

    def set_style(self, style: str):
        if style in self.__style_map:
            self.__list_widget.set_item(self.__style_map[style])

    def update_language(self):
        self.setWindowTitle(tr.style())
        self.__list_widget.update_language()
