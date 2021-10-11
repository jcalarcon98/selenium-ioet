from typing import Tuple
from typing import Optional

from selenium.common.exceptions import NoSuchElementException


class DriverWrapper:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator: Tuple[str, str]):
        elements = self.driver.find_elements(*locator)
        return elements

    def find_element(self, locator: Tuple[str, str]):
        element = self.driver.find_element(*locator)
        return element

    def get_element_text(self, locator: Tuple[str, str]) -> Optional[str]:
        try:
            element = self.find_element(locator)
        except NoSuchElementException:
            return None
        return element.text

    def exists_element(self, locator: Tuple[str, str]) -> bool:
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def get_element_attribute(self, locator: Tuple[str, str], attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def open_tab(self):
        open_new_tab_command = 'window.open('');'
        self.driver.execute_script(open_new_tab_command)

    def switch_to_window(self, window_number: int):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    def visit_page(self, page_link: str):
        self.driver.get(page_link)

    def close_current_page(self):
        self.driver.close()

    def click(self, locator):
        self.driver.find_element(*locator).click()

