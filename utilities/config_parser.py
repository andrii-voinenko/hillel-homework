import configparser
from CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f"{ROOT_DIR}/configurations/configuration.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_username():
        return config.get('user_info', 'user_name')

    @staticmethod
    def get_password():
        return config.get('user_info', 'password')

    @staticmethod
    def get_browser_id():
        return config.get('browser', 'browser_id')
