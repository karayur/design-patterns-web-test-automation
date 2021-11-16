from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LOCATOR_SEARCH_INPUT = (By.CLASS_NAME, "search-form__search")


class SearchProjectsPage(BasePage):

    def search_for(self, word):
        search_field = self.find_element(LOCATOR_SEARCH_INPUT)
        search_field.send_keys(word + Keys.RETURN)
        return self.driver



