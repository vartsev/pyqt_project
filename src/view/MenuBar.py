from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMenuBar, qApp, QAction
from src.utils.Translator import Translator

tr = Translator.inst()


class MenuBar(QMenuBar):
    action_signal = pyqtSignal(str)
    language_signal = pyqtSignal(str)

    def __init__(self):
        QMenuBar.__init__(self)

        self.__exit_action = QAction(tr.exit(), self)
        self.__exit_action.setShortcut('Ctrl+Q')
        self.__exit_action.triggered.connect(qApp.quit)

        self.__first_menu = self.addMenu(tr.first_menu())
        self.__first_menu.addAction(self.__exit_action)

        self.__second_menu = self.addMenu(tr.second_menu())
        self.__action_1 = QAction(tr.action_1(), self)
        self.__action_2 = QAction(tr.action_2(), self)
        self.__action_3 = QAction(tr.action_3(), self)
        self.__second_menu.addAction(self.__action_1)
        self.__sub_menu = self.__second_menu.addMenu(tr.sub_menu())
        self.__sub_menu.addAction(self.__action_2)
        self.__sub_menu.addAction(self.__action_3)
        self.__action_1.triggered.connect(lambda: self.action_signal.emit(self.__action_1.text()))
        self.__action_2.triggered.connect(lambda: self.action_signal.emit(self.__action_2.text()))
        self.__action_3.triggered.connect(lambda: self.action_signal.emit(self.__action_3.text()))

        self.__language_menu = self.addMenu(tr.language())
        self.__english_action = QAction(tr.english(), self, checkable=True)
        self.__russian_action = QAction(tr.russian(), self, checkable=True)
        self.__language_menu.addAction(self.__english_action)
        self.__language_menu.addAction(self.__russian_action)

        self.__english_action.triggered.connect(lambda: self.update_language_menu('en'))
        self.__russian_action.triggered.connect(lambda: self.update_language_menu('ru'))

    def update_language(self):
        self.__first_menu.setTitle(tr.first_menu())
        self.__exit_action.setText(tr.exit())
        self.__second_menu.setTitle(tr.second_menu())
        self.__sub_menu.setTitle(tr.sub_menu())
        self.__action_1.setText(tr.action_1())
        self.__action_2.setText(tr.action_2())
        self.__action_3.setText(tr.action_3())
        self.__language_menu.setTitle(tr.language())
        self.__english_action.setText(tr.english())
        self.__russian_action.setText(tr.russian())

    def update_language_menu(self, lang: str):
        if lang == 'en':
            self.__english_action.setChecked(True)
            self.__russian_action.setChecked(False)
            self.language_signal.emit('en')
        else:
            self.__english_action.setChecked(False)
            self.__russian_action.setChecked(True)
            self.language_signal.emit('ru')
