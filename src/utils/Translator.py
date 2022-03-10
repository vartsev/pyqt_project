class Translator:
    __instance = None

    @staticmethod
    def inst():
        if Translator.__instance is None:
            Translator.__instance = Translator()
        return Translator.__instance

    def __init__(self):
        super().__init__()
        self.__lang = 'en'

        self.__qt_project = {'en': 'Qt Project', 'ru': 'Qt Проект'}

        self.__style = {'en': 'Style', 'ru': 'Стиль'}
        self.__grey = {'en': 'Grey', 'ru': 'Серый'}
        self.__red = {'en': 'Red', 'ru': 'Красный'}
        self.__green = {'en': 'Green', 'ru': 'Зеленый'}
        self.__blue = {'en': 'Blue', 'ru': 'Голубой'}

        self.__first_menu = {'en': '&First menu', 'ru': '&Первое меню'}
        self.__exit = {'en': 'Exit', 'ru': 'Выход'}
        self.__second_menu = {'en': '&Second menu', 'ru': '&Второе меню'}
        self.__sub_menu = {'en': '&Sub menu', 'ru': '&Подменю'}
        self.__action_1 = {'en': 'Action 1', 'ru': 'Действие 1'}
        self.__action_2 = {'en': 'Action 2', 'ru': 'Действие 2'}
        self.__action_3 = {'en': 'Action 3', 'ru': 'Действие 3'}
        self.__language = {'en': '&Language', 'ru': '&Язык'}
        self.__english = {'en': 'English', 'ru': 'Английский'}
        self.__russian = {'en': 'Russian', 'ru': 'Русский'}

        self.__hide_style_panel = {'en': 'Hide style panel', 'ru': 'Скрыть панель стилей'}
        self.__show_style_panel = {'en': 'Show style panel', 'ru': 'Показать панель стилей'}
        self.__hide_table = {'en': 'Hide table', 'ru': 'Скрыть таблицу'}
        self.__show_table = {'en': 'Show table', 'ru': 'Показать таблицу'}
        self.__hide_text_panel = {'en': 'Hide text panel', 'ru': 'Скрыть текстовую панель'}
        self.__show_text_panel = {'en': 'Show text panel', 'ru': 'Показать текстовую панель'}
        self.__clear_text_fields = {'en': 'Clear text fields', 'ru': 'Очистить текстовые поля'}
        self.__add_text_field = {'en': 'Add text field', 'ru': 'Добавить текстовое поле'}

        self.__parameter = {'en': 'Parameter', 'ru': 'Параметр'}
        self.__value = {'en': 'Value', 'ru': 'Значение'}
        self.__add_line = {'en': 'Add line', 'ru': 'Добавить строку'}
        self.__del_line = {'en': 'Delete line', 'ru': 'Удалить строку'}

        self.__text = {'en': 'Text', 'ru': 'Текст'}

    def set_language(self, language: str):
        self.__lang = language

    def get_language(self) -> str:
        return self.__lang

    def qt_project(self) -> str:
        return self.__qt_project[self.__lang]

    def style(self) -> str:
        return self.__style[self.__lang]

    def grey(self) -> str:
        return self.__grey[self.__lang]

    def red(self) -> str:
        return self.__red[self.__lang]

    def green(self) -> str:
        return self.__green[self.__lang]

    def blue(self) -> str:
        return self.__blue[self.__lang]

    def first_menu(self) -> str:
        return self.__first_menu[self.__lang]

    def exit(self) -> str:
        return self.__exit[self.__lang]

    def second_menu(self) -> str:
        return self.__second_menu[self.__lang]

    def sub_menu(self) -> str:
        return self.__sub_menu[self.__lang]

    def action_1(self) -> str:
        return self.__action_1[self.__lang]

    def action_2(self) -> str:
        return self.__action_2[self.__lang]

    def action_3(self) -> str:
        return self.__action_3[self.__lang]

    def language(self) -> str:
        return self.__language[self.__lang]

    def english(self) -> str:
        return self.__english[self.__lang]

    def russian(self) -> str:
        return self.__russian[self.__lang]

    def hide_style_panel(self) -> str:
        return self.__hide_style_panel[self.__lang]

    def show_style_panel(self) -> str:
        return self.__show_style_panel[self.__lang]

    def hide_table(self) -> str:
        return self.__hide_table[self.__lang]

    def show_table(self) -> str:
        return self.__show_table[self.__lang]

    def hide_text_panel(self) -> str:
        return self.__hide_text_panel[self.__lang]

    def show_text_panel(self) -> str:
        return self.__show_text_panel[self.__lang]

    def clear_text_fields(self) -> str:
        return self.__clear_text_fields[self.__lang]

    def add_text_field(self) -> str:
        return self.__add_text_field[self.__lang]

    def parameter(self) -> str:
        return self.__parameter[self.__lang]

    def value(self) -> str:
        return self.__value[self.__lang]

    def add_line(self) -> str:
        return self.__add_line[self.__lang]

    def del_line(self) -> str:
        return self.__del_line[self.__lang]

    def text(self) -> str:
        return self.__text[self.__lang]
