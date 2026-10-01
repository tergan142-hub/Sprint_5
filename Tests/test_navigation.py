from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
from locators import Button_on_main_paige

class Test_navigation:
    def test_button_Enter_to_account(self, driver):

        driver.get(Data.SB_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Button_on_main_paige. Account_button))

        account_button = driver.find_element(*Button_on_main_paige.Account_button)
        account_button.click()
        assert driver.current_url == Data.SB_login_url

    def test_button_personal_account(self, driver):

        driver.get(Data.SB_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Button_on_main_paige. Account_button))

        personal_account = driver.find_element(*Button_on_main_paige.Personal_account)
        personal_account.click()
        assert driver.current_url == Data.SB_login_url

    def test_registration_button(self, driver):

        driver.get(Data.SB_login_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.SB_registration_button_second))

        registration_button = driver.find_element(*RegistrationLocators.SB_registration_button_second)
        registration_button.click()
        assert driver.current_url == Data.SB_registration

    def test_recover_password(self, driver):

        driver.get(Data.SB_login_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.SB_registration_button_second))

        recovery_button = driver.find_element(*RegistrationLocators.SB_recovery_button)
        recovery_button.click()
        assert driver.current_url == Data.SB_recovery_password