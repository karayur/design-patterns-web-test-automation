from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LOCATOR_SEARCH_RESULTS_ITEMS = (By.CSS_SELECTOR, "ul[aria-label='Search results']>li")

LOCATOR_SEARCH_RESULTS_PROJECT_NAMES = (By.CSS_SELECTOR, "li span.package-snippet__name")


class SearchResultsPage(BasePage):

    def get_projects_count(self):
        count = len(self.find_elements(LOCATOR_SEARCH_RESULTS_ITEMS))

        return count

    def click_on_first_project(self):
        self.find_elements(LOCATOR_SEARCH_RESULTS_ITEMS)[0].click()

    def count_matched_projects_on_the_page(self, string_to_match: str):
        project_items = self.find_elements(LOCATOR_SEARCH_RESULTS_PROJECT_NAMES)
        project_names = [el.text for el in project_items]
