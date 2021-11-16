from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

LOCATOR_SEARCH_RESULTS_ITEMS = (By.CSS_SELECTOR, "ul[aria-label='Search results']>li")
LOCATOR_SEARCH_RESULTS_PROJECT_NAMES = (By.CSS_SELECTOR, "li span.package-snippet__name")
LOCATOR_SEARCH_RESULTS_PROJECT_LINKS = (By.CSS_SELECTOR, "li>a.package-snippet")


class SearchResultsPage(BasePage):

    def get_first_project_name(self):
        return self.find_elements(LOCATOR_SEARCH_RESULTS_ITEMS)[0].text

    def get_first_project_url(self):
        return self.find_elements(LOCATOR_SEARCH_RESULTS_PROJECT_LINKS)[0].get_attribute("href")

    def get_projects_count(self):

        return len(self.find_elements(LOCATOR_SEARCH_RESULTS_ITEMS))

    def click_on_first_project(self):
        self.find_elements(LOCATOR_SEARCH_RESULTS_ITEMS)[0].click()
        return self.driver


    # def count_matched_projects_on_the_page(self, string_to_match: str):
    #     project_items = self.find_elements(LOCATOR_SEARCH_RESULTS_PROJECT_NAMES)
    #     project_names = [el.text for el in project_items]
