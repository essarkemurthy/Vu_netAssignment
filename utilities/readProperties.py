import configparser

config = configparser.RawConfigParser()
config.read("../Configurations/config.ini")


class ReadConfig():
    @staticmethod
    def get_application_url(self):
        url = config.get("common_info", "baseURL")
        return url
