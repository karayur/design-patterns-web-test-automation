from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.login_register.username_password_base import UsernamePasswordBase

LOCATOR_NAME = (By.ID, "name")
LOCATOR_EMAIL = (By.ID, "email")
LOCATOR_PASSWORD = (By.ID, "new_password")
LOCATOR_PASSWORD_CONFIRM = (By.ID, "password_confirm")


class Register(UsernamePasswordBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.password_confirm = self.find_element(LOCATOR_PASSWORD_CONFIRM)
        self.password = self.find_element(LOCATOR_PASSWORD)

    def enter_name(self, name):
        self.name.send_keys(name)

    def enter_email(self, email):
        self.email.send_keys(email)

    def enter_password_confirm(self, password):
        self.password_confirm.send_keys(password)

    def is_password_confirm_masked(self):
        input_attr_type_value = self.password_confirm.get_attribute("type")
        if input_attr_type_value == "password":
            return True
        else:
            return False
