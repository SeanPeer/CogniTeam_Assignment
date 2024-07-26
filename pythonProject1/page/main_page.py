from selenium.webdriver.common.by import By

from utils.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.elements = {
            'categories': [By.XPATH, """//div[@id='mainContent']/div[2]/div[2]/div/div/div/ul/li/a/h3"""],
            'search_bar': [By.XPATH, """//header/table/tbody/tr/td[3]/form/table/tbody/tr/td/div/div/input[1]"""],
            'search_button': [By.XPATH, """//header/table/tbody/tr/td[4]/input"""],
            'results': [By.XPATH, """//div[@id='mainContent']/div[3]/div/div[3]/ul/li/div/div[2]/a/div/span"""],



        }

