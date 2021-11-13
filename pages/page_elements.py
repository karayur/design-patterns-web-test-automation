from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, web_element: WebElement):
        self._web_element = web_element


class CheckBox(BaseElement):

    def is_checked(self):
        return self._web_element.is_selected()

    def toggle(self):
        self._web_element.click()
        return


class PasswordInputBox(BaseElement):

    def is_type_password(self):
        input_attr_type_value = self._web_element.get_attribute("type")
        if input_attr_type_value == "password":
            return True
        else:
            return False
