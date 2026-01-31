import configparser  #to read config_SIT.ini file

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config_SIT.ini")

class ReadProperties:
    @staticmethod
    def get_data_for_email():
        return config.get("login_data","email")

    @staticmethod
    def get_data_for_password():
        return config.get("login_data","password")

    @staticmethod
    def get_login_url():
        return config.get("application_url","login_url")

    @staticmethod
    def get_registration_url():
        return config.get("application_url","registration_url")
