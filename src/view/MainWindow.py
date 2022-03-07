from PyQt5.QtWidgets import QMainWindow, QListWidgetItem
from PyQt5.QtCore import QSize, Qt

from src.view.CentralWidget import CentralWidget
from src.view.MenuBar import MenuBar
from src.view.StyleWidget import StyleWidget
from src.view.StatusBar import StatusBar
from src.utils.Translator import Translator
from src.utils.Config import Config

tr = Translator.inst()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        lang = Config.inst().get_lang()
        tr.set_language(lang)

        self.set_style(Config.inst().get_style())
        self.setMinimumSize(QSize(600, 400))

        self.__style_widget = StyleWidget(self)
        self.__style_widget.visibilityChanged.connect(self.change_style_button_name)
        self.__style_widget.set_style(Config.inst().get_style())
        self.__style_widget.style_changed.connect(self.set_style)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.__style_widget)

        self.__central_widget = CentralWidget()
        self.__central_widget.style_panel_changed.connect(self.change_dock_widget)
        self.setCentralWidget(self.__central_widget)

        status_bar = StatusBar()
        self.setStatusBar(status_bar)

        self.__menu_bar = MenuBar()
        self.setMenuBar(self.__menu_bar)
        self.__menu_bar.update_language_menu(Config.inst().get_lang())
        self.__menu_bar.action_signal.connect(status_bar.showMessage)
        self.__menu_bar.language_signal.connect(self.update_language)

        self.__central_widget.text_fields_widget.text_signal.connect(status_bar.showMessage)

        self.init_language(lang)

    def init_language(self, lang: str):
        tr.set_language(lang)
        self.setWindowTitle(tr.qt_project())
        self.__style_widget.update_language()
        self.__central_widget.update_language()
        self.__menu_bar.update_language()

        if self.__style_widget.isVisible():
            self.__central_widget.set_style_panel_name(tr.hide_style_panel()
                                                       if self.__style_widget.isVisible()
                                                       else tr.show_style_panel()
                                                       )

    def update_language(self, lang: str):
        if Config.inst().get_lang() != lang:
            self.init_language(lang)
            Config.inst().set_lang(lang)

    def change_dock_widget(self):
        if self.__style_widget.isHidden():
            self.__style_widget.show()
        else:
            self.__style_widget.hide()
        self.change_style_button_name()

    def change_style_button_name(self):
        if self.__style_widget.isVisible():
            self.__central_widget.set_style_panel_name(tr.hide_style_panel())
        else:
            self.__central_widget.set_style_panel_name(tr.show_style_panel())

    def set_style(self, style: str):
        with open(self.get_path_by_style(style), 'r') as f:
            self.setStyleSheet(f.read())
            Config.inst().set_style(style)

    @staticmethod
    def get_path_by_style(style: str):
        return 'config/' + style.lower() + '.stylesheet'
