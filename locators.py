from selenium.webdriver.common.by import By

#локатор для входа через кнопку «Личный кабинет»
class LoginPageLocators:
    
    SB_email_field = (By.XPATH, "//input[@type='text']")

    SB_password_field = (By.XPATH, "//input[@type='password']")

    SB_login_button = (By.XPATH, '//button[text()="Войти"]')

 
class RegistrationLocators:

    SB_name_field = (By.XPATH, "(//input[@name='name'])[1]")

    SB_email_field = (By.XPATH, "(//input[@name='name'])[2]")
    SB_email_field_second = (By.XPATH, "//input[@name='name']")
    
    SB_password_field = (By.XPATH, "//input[@type='password']")
    SB_password_field_second = (By.XPATH, "//input[@type='password']")

    SB_registration_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    SB_registration_button_second = (By.XPATH, "//a[@href='/register']")

    SB_password_error = (By.XPATH, "//p[@class='input__error text_type_main-default']")

    SB_recovery_button = (By.XPATH, "//a[text()='Восстановить пароль']")


class Button_on_main_paige:

    Account_button = (By.XPATH, "//button[text()='Войти в аккаунт']")

    Personal_account = (By.XPATH, "//p[text()='Личный Кабинет']")

    Buns_button = (By.XPATH, "//div[span[text()='Булки']]")
    Buns_button_active = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__') and span[text()='Булки']]")
    
    Sauce_button = (By.XPATH, "//div[span[text()='Соусы']]")
    Sauce_button_active = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__') and span[text()='Соусы']]")

    Fillings_button = (By.XPATH, "//div[span[text()='Начинки']]")
    Fillings_button_active = (By.XPATH, "//div[contains(@class,'tab_tab_type_current__') and span[text()='Начинки']]")

class Img_on_main_page:

    Buns = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")

    Sauce = (By.XPATH, "//img[@alt='Соус Spicy-X']")

    Fillings = (By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']")


class Personal_account:

    Name_field = (By.XPATH, "//input[@name='Name']")

    Constructor = (By.XPATH, "//p[text()='Конструктор']")

    Logotype = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    Exit_button = (By.XPATH, "//button[@type='button' and text()='Выход']")