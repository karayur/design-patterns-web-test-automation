import pytest

from tests.test_data import *
from pages.project.project_header import ProjectHeaderPage
from pages.search.search_projects import SearchProjectsPage
from pages.search.search_results import SearchResultsPage


@pytest.fixture()
def search_projects(browser):
    browser.get(SITE_BASE_URL)
    return SearchProjectsPage(browser)


def test_search_open_proper_search_url(browser):
    browser.get(SITE_BASE_URL)  # NOT using fixture for ARRANGE
    search_for_projects = SearchProjectsPage(browser)

    search_for_projects.search_for(DEFAULT_PROJECT_NAME)

    search_url = browser.current_url
    assert search_url == SITE_BASE_URL + SEARCH_PATH + DEFAULT_PROJECT_NAME


def test_search_results_show_relevant_projects(browser):
    browser.get(SITE_BASE_URL + SEARCH_PATH + DEFAULT_PROJECT_NAME)
    search_results = SearchResultsPage(browser)

    search_results.click_on_first_project()

    project_name = ProjectHeaderPage(browser).get_project_name()
    assert DEFAULT_PROJECT_NAME.lower() in project_name.lower()
