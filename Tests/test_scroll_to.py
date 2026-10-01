from data import Data
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Button_on_main_paige
from locators import Img_on_main_page

class Test_sroll_to:

    def test_sroll_to_sauce(self, driver):
        driver.get(Data.SB_url)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Img_on_main_page.Buns))

        sauce = driver.find_element(*Button_on_main_paige.Sauce_button)
        sauce.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Img_on_main_page.Sauce))

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Button_on_main_paige.Sauce_button_active))

    def test_sroll_to_fillings(self, driver):
        driver.get(Data.SB_url)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Img_on_main_page.Buns))

        fillings = driver.find_element(*Button_on_main_paige.Fillings_button)
        fillings.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Img_on_main_page.Fillings))

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Button_on_main_paige.Fillings_button_active))

    def test_sroll_to_buns(self, driver):
        driver.get(Data.SB_url)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Img_on_main_page.Buns))

        fillings = driver.find_element(*Button_on_main_paige.Fillings_button)
        fillings.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Img_on_main_page.Fillings))

        buns = driver.find_element(*Button_on_main_paige.Buns_button)
        buns.click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Img_on_main_page.Buns))

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Button_on_main_paige.Buns_button_active))