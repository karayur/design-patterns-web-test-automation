from selenium.webdriver.remote.webelement import WebElement


class BaseElement(WebElement):
    def __init__(self, element):
        super().__init__(element.parent, element.id)


class CheckBox(BaseElement):

    def is_checked(self):
        return self.is_selected()

    def toggle(self):
        self.click()
        return


class PasswordInputBox(BaseElement):
    def is_type_password(self):
        input_attr_type_value = self.get_attribute("type")
        if input_attr_type_value == "password":
            return True
        else:
            return False
