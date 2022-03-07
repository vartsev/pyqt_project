from PyQt5.QtWidgets import QStatusBar


class StatusBar(QStatusBar):
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QStatusBar.__init__(self)

    def show_message(self, text: str):
        self.status_bar.showMessage(text, 2000)
