from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LOCATOR_SEARCH_RESULTS_ITEMS = (By.CSS_SELECTOR, "ul[aria-label='Search results']>li")


class SearchResults(BasePage):

    def get_projects_count(self):
        count = len(self.find_elements(LOCATOR_SEARCH_RESULTS_ITEMS))

        return count

    def click_on_first_project(self):
        self.find_elements(LOCATOR_SEARCH_RESULTS_ITEMS)[0].click()

