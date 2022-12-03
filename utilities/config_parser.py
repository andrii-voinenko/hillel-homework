from CONSTANTS import ROOT_DIR
import configparser

config = configparser.RawConfigParser()
config.read(f"{ROOT_DIR}/configurations/configuration.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_creds():
        creds = (config.get('user_info', 'user_name'), config.get('user_info', 'password'))
        return creds

    @staticmethod
    def get_creds_locked():
        creds = (config.get('user_info', 'user_locked'), config.get('user_info', 'password'))
        return creds

