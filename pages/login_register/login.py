from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.controls import CheckBox
from pages.login_register.username_password_base import UsernamePasswordBase

LOCATOR_PASSWORD = (By.ID, "password")


class Login(UsernamePasswordBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.password = self.find_element(LOCATOR_PASSWORD)


