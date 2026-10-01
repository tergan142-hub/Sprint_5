from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators


class Test_login:
    def test_login(self, driver):
        #Открытие страницы со входом в ЛК
        driver.get(Data.SB_login_url)

        #Обязательно подождать появление элементов на странице (поле email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPageLocators.SB_email_field))

        #поиск поля email и сохранение в переменную
        email_field = driver.find_element(*LoginPageLocators.SB_email_field)

        #очистка поля email и ввод почты
        email_field.clear()
        email_field.send_keys(Data.Email)

        #проверка, что поле email заполненно
        assert email_field.get_attribute("value") == Data.Email

        #поиск поля password и сохранение в переменную
        password_field = driver.find_element(*LoginPageLocators.SB_password_field)

        #очистка поля password и ввод почты
        password_field.clear()
        password_field.send_keys(Data.Password)

        #проверка, что поле password заполненно
        assert password_field.get_attribute("value") == Data.Password

        #поиск кнопки Войти, сохранение в переменную, нажатие
        login_button = driver.find_element(*LoginPageLocators.SB_login_button)
        login_button.click()

        #Обязательно подождать перехода на главную страницу, проверка по url, что переход выполнен
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.SB_url))
        assert driver.current_url == Data.SB_url