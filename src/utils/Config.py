import configparser
import os


class Config:
    __instance = None

    @staticmethod
    def inst():
        if Config.__instance is None:
            Config.__instance = Config()
        return Config.__instance

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.__config_path = 'config/conf.ini'
        if not os.path.isfile(self.__config_path):
            e = FileExistsError(f'Config file not found at {self.__config_path}')
            raise e
        self.conf.read(self.__config_path)

    def get_style(self):
        return self.conf.get('view', 'style')

    def set_style(self, style: str):
        self.conf.set('view', 'style', style)
        with open(self.__config_path, 'w') as configfile:
            self.conf.write(configfile)

    def get_lang(self):
        return self.conf.get('view', 'lang')

    def set_lang(self, lang: str):
        self.conf.set('view', 'lang', lang)
        with open(self.__config_path, 'w') as configfile:
            self.conf.write(configfile)
