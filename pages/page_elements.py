import selenium.webdriver.remote.webelement


class BaseElement:
    def __init__(self, web_element: selenium.webdriver.remote.webelement.WebElement):
        self._web_element = web_element


class Button(BaseElement):
    def click(self):
        self._web_element.click()


class CheckBox(BaseElement):

    def is_checked(self):
        return self._web_element.is_selected()

    def toggle(self):
        self._web_element.click()


class InputBox(BaseElement):

    def enter_text(self, password):
        self._web_element.send_keys(password)


class PasswordInput(InputBox):

    def is_type_password(self) -> bool:
        input_attr_type_value = self._web_element.get_attribute("type")
        return input_attr_type_value == "password"
