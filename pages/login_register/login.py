from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.checkbox import CheckBox

LOCATOR_USERNAME_INPUT = (By.ID, "username")
LOCATOR_PASSWORD_INPUT = (By.ID, "password")
LOCATOR_SHOW_PASSWORD_CHECKBOX = (By.ID, "show-password")
LOCATOR_PASSWORD_INPUT


class Login(BasePage):

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, username):
        self.find_element(LOCATOR_USERNAME_INPUT).send_keys(username)

    def enter_user_password(self, password):
        self.find_element(LOCATOR_PASSWORD_INPUT).send_keys(password)

    def toggle_show_password(self):
        self.find_element(LOCATOR_SHOW_PASSWORD_CHECKBOX).toggle()

    def is_password_hidden(self):
        input_attr_type_value = self.find_element(LOCATOR_PASSWORD_INPUT).get_attribute("type")
        if input_attr_type_value == "password":
            return True
        else:
            return False
