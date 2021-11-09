from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Search4Projects(BasePage):

    def search_for_keyword(self, word):
        search_field = self.find_element((By.CLASS_NAME,"search-form__search"))
        search_field.click()
        search_field.send_keys(word + Keys.RETURN)
        return search_field

    # def click_on_the_search_button(self):
    #     return

