import random
import string


class Data:
    SB_url = "https://stellarburgers.education-services.ru/"
    SB_login_url = "https://stellarburgers.education-services.ru/login"
    SB_registration = "https://stellarburgers.education-services.ru/register"
    SB_recovery_password = "https://stellarburgers.education-services.ru/forgot-password"
    SB_personal_account = "https://stellarburgers.education-services.ru/account"

    Name = "Vlad"
    Email = "Vladimir_Izmestev_55_777@yandex.ru"
    Password = "Rejim123"

    invalid_password = [("1_symbol", "q"), ("5_symbols", "qwert")]

    @staticmethod
    def unique_name():
        return 'Vlad_' + ''.join(random.choices(string.ascii_lowercase, k=6))

    @staticmethod
    def unique_email():
        return 'vlad_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '@yandex.ru'

    @staticmethod
    def unique_password():
        return 'Rejim' + ''.join(random.choices(string.digits, k=4))