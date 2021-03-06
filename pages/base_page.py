from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: object, time: object = 10) -> WebElement:
        return WebDriverWait(self.driver, time) \
            .until(EC.presence_of_element_located(locator),
                   message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10) -> List['WebElement']:
        return WebDriverWait(self.driver, time) \
            .until(EC.presence_of_all_elements_located(locator),
                   message=f"Can't find elements by locator {locator}")

    # def wait_for_ajax(self, time=10):
    #   WebDriverWait(self.driver, time=10) \
    #       .until(lambda d: d.execute_script("return jQuery.active == 0"))

    # def wait_until_page_loads_completely(self, time=10):
    #   WebDriverWait(driver, time=10) \
    #       .until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    # self.driver.delete_all_cookies()
