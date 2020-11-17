import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get("common_info", "baseURL")
        return url
