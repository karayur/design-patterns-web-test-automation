from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.controls import CheckBox

LOCATOR_USERNAME = (By.ID, "username")
LOCATOR_PASSWORD = None  # to define in child class
LOCATOR_SHOW_PASSWORD_CHECKBOX = (By.ID, "show-password")


class UsernamePasswordBase(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.username = self.find_element(LOCATOR_USERNAME)
        self.password = None  # to define in child class
        self.show_password_chk = CheckBox(self.find_element(LOCATOR_SHOW_PASSWORD_CHECKBOX))

    def enter_user_name(self, username):
        self.username.send_keys(username)

    def enter_password(self, password):
        self.password.send_keys(password)

    def toggle_show_password(self):
        self.show_password_chk.toggle()

    def is_password_masked(self):

        input_attr_type_value = self.password.get_attribute("type")
        if input_attr_type_value == "password":
            return True
        else:
            return False



