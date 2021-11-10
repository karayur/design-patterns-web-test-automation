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


