from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
from locators import Button_on_main_paige
from locators import LoginPageLocators

class Test_personal_accoutn_button:
    def test_personal_account_button(self, driver):

        driver.get(Data.SB_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Button_on_main_paige.Personal_account))

        personal_account_button = driver.find_element(*Button_on_main_paige.Personal_account)
        personal_account_button.click()
        assert driver.current_url == Data.SB_login_url

        email_feild = driver.find_element(*RegistrationLocators.SB_email_field_second)
        email_feild.send_keys(Data.Email)

        password_field = driver.find_element(*RegistrationLocators.SB_password_field_second)
        password_field.send_keys(Data.Password)

        enter_button = driver.find_element(*LoginPageLocators.SB_login_button)
        enter_button.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Data.SB_url))

        personal_account_button.click()
        assert driver.current_url == Data.SB_personal_account