from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.custom_web_elements import CheckBox, PasswordInputBox

# general locators
LOCATOR_USERNAME = (By.ID, "username")
LOCATOR_SHOW_PASSWORD_CHECKBOX = (By.ID, "show-password")

# Login specific locators
LOCATOR_PASSWORD_LOGIN = (By.ID, "password")
LOCATOR_LOG_IN_BTN = (By.CSS_SELECTOR, 'input[value="Log in"]')

# Register specific locators
LOCATOR_NAME = (By.ID, "name")
LOCATOR_EMAIL = (By.ID, "email")
LOCATOR_PASSWORD_REGISTER = (By.ID, "new_password")
LOCATOR_PASSWORD_CONFIRM = (By.ID, "password_confirm")
LOCATOR_CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, 'input[data-target="password-match.submit"]')


class UsernamePasswordMixin:

    def enter_user_name(self, username):
        self.username.send_keys(username)

    def enter_password(self, password):
        self.password.send_keys(password)

    def toggle_show_password(self):
        self.show_password_checkbox.toggle()

    def is_password_masked(self):
        return self.password.is_type_password()

    # def _is_type_password(self, input_web_element):
    #     input_attr_type_value = input_web_element.get_attribute("type")
    #     if input_attr_type_value == "password":
    #         return True
    #     else:
    #         return False


class Login(BasePage, UsernamePasswordMixin):

    def __init__(self, driver):
        super().__init__(driver)
        self.username = self.find_element(LOCATOR_USERNAME)
        self.password = PasswordInputBox(self.find_element(LOCATOR_PASSWORD_LOGIN))
        self.show_password_checkbox = CheckBox(self.find_element(LOCATOR_SHOW_PASSWORD_CHECKBOX))
        self.log_in_btn = self.find_element(LOCATOR_LOG_IN_BTN)


class Register(BasePage, UsernamePasswordMixin):
    def __init__(self, driver):
        super().__init__(driver)
        self.name = self.find_element(LOCATOR_PASSWORD_CONFIRM)
        self.email = self.find_element(LOCATOR_PASSWORD_REGISTER)
        self.password = PasswordInputBox(self.find_element(LOCATOR_PASSWORD_REGISTER))
        self.confirm_password = PasswordInputBox(self.find_element(LOCATOR_PASSWORD_CONFIRM))
        self.show_password_checkbox = CheckBox(self.find_element(LOCATOR_SHOW_PASSWORD_CHECKBOX))
        self.create_account_btn = self.find_element(LOCATOR_CREATE_ACCOUNT_BTN)

    def enter_name(self, name):
        self.name.send_keys(name)

    def enter_email(self, email):
        self.email.send_keys(email)

    def enter_password_confirm(self, password):
        self.confirm_password.send_keys(password)

    def is_password_confirm_masked(self):
        return self.confirm_password.is_type_password()
