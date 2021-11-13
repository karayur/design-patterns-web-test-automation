from pages.base_page import BasePage
from selenium.webdriver.common.by import By


LOCATOR_PROJECT_HEADER_NAME = (By.CLASS_NAME, "package-header__name")


class ProjectHeader(BasePage):

    def get_project_name(self):
        return self.find_element(LOCATOR_PROJECT_HEADER_NAME).text


