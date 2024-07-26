from selenium.webdriver.common.by import By
from utils.helpers import safe_click, safe_read, safe_find_element, safe_send_keys, safe_frame_switch, safe_find_elements


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.elements = {}

    def find_element(self, key, wait_for_visibility=True):
        value = self.elements[key][1]
        return safe_find_element(self.driver, self.elements[key][0], value, wait_for_visibility)

    def find_elements(self, key, wait_for_visibility=True):
        value = self.elements[key][1]
        return safe_find_elements(self.driver, self.elements[key][0], value, wait_for_visibility)

    def click(self, element):
        if element:
            return safe_click(element)
        else:
            return None

    def read_text(self, element):
        if element:
            return safe_read(element)
        return None

    def send_keys(self, element, keys):
        if element:
            return safe_send_keys(element, keys)

    def switch_to_correct_frame(self, key) -> None:
        value = self.elements[key][1]
        by = self.elements[key][0]
        return safe_frame_switch(self.driver, by, value)
