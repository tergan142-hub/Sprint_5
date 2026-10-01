from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
from locators import Button_on_main_paige
from locators import LoginPageLocators
from locators import Personal_account

class Test_exit_button:
    def test_exit_button(self, driver):
        driver.get(Data.SB_login_url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.SB_password_field))
        
        email_field = driver.find_element(*LoginPageLocators.SB_email_field)
        email_field.clear()
        email_field.send_keys(Data.Email)
                
        password_field = driver.find_element(*LoginPageLocators.SB_password_field)
        password_field.clear()
        password_field.send_keys(Data.Password)
                
        login_button = driver.find_element(*LoginPageLocators.SB_login_button)
        login_button.click()
               
        personal_account = driver.find_element(*Button_on_main_paige.Personal_account)
        personal_account.click()

        exit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Personal_account.Exit_button))    
        exit_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Data.SB_login_url))
        assert driver.current_url == Data.SB_login_url