import pytest
from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators

class Test_registration:
    def test_registration(self, driver):
        name = Data.unique_name()
        email = Data.unique_email()
        password = Data.unique_password()

        #переход на страницу сайта
        driver.get(Data.SB_registration)

        #ожидание загрузки страницы
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.SB_registration_button))

        #поиск, заполнение, проверка поля Имя
        name_field = driver.find_element(*RegistrationLocators.SB_name_field)
        name_field.clear()
        name_field.send_keys(name)
        assert name_field.get_attribute('value') == name

        #поиск, заполнение, проверка поля Email
        email_field = driver.find_element(*RegistrationLocators.SB_email_field)
        email_field.clear()
        email_field.send_keys(email)
        assert email_field.get_attribute('value') == email

        #поиск, заполнение, проверка поля Пароль
        password_field = driver.find_element(*RegistrationLocators.SB_password_field)
        password_field.clear()
        password_field.send_keys(password)
        assert password_field.get_attribute('value') == password

        #поиск и нажатие на кнопку Регистрации
        registration_button = driver.find_element(*RegistrationLocators.SB_registration_button)
        registration_button.click()

        #ожидание загрузки страницы
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.SB_login_url))

        #проверка что регистрация прошла
        assert driver.current_url == Data.SB_login_url


    @pytest.mark.parametrize("password", ["q", "qwert"])
    def test_registration_with_invalid_password(self, driver, password):

        name = Data.unique_name()
        email = Data.unique_email()
        
        #переход на страницу и ожидание ее загрузки
        driver.get(Data.SB_registration)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.SB_registration_button))

        #поиск и заполнение полей имя, email, пароль, а также нажатие на кнопку Регистрации
        driver.find_element(*RegistrationLocators.SB_name_field).send_keys(name)
        driver.find_element(*RegistrationLocators.SB_email_field).send_keys(email)
        driver.find_element(*RegistrationLocators.SB_password_field).send_keys(password)
        driver.find_element(*RegistrationLocators.SB_registration_button).click()

        #ожидание загрузки страницы с поиском элемента на страницы
        error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.SB_password_error))

        #проверка того, что в форме регистрации правильно введен невалидный пароль
        assert error.text == "Некорректный пароль"
        assert driver.current_url == Data.SB_registration

    