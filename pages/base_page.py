from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: object, time: object = 10) -> object:
        return WebDriverWait(self.driver, time) \
            .until(EC.presence_of_element_located(locator),
                message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time) \
            .until(EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}")

    # def get_element_attribute(self, locator, attribute_name):
    #     return = WebDriverWait(self.driver, time).until(
    #         EC.element_to_be_clickable((By.ID, "org"))).get_attribute(
    #         "attribute_name")
