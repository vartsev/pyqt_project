from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget
from src.utils.Translator import Translator

tr = Translator.inst()


class ListWidget(QListWidget):
    def __init__(self):
        QListWidget.__init__(self)

        self.addItem(tr.grey())
        self.addItem(tr.red())
        self.addItem(tr.green())
        self.addItem(tr.blue())

    def update_language(self):
        self.item(0).setText(tr.grey())
        self.item(1).setText(tr.red())
        self.item(2).setText(tr.green())
        self.item(3).setText(tr.blue())
        pass

    def set_item(self, item_number: int):
        self.setCurrentItem(self.item(item_number))
