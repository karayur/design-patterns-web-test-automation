import pytest

from tests.test_data import *
from pages.search.search_projects import SearchProjectsPage
from pages.search.search_results import SearchResultsPage


@pytest.fixture()
def search_projects(browser):
    browser.get(SITE_BASE_URL)
    return SearchProjectsPage(browser)


def test_search_opens_proper_search_url(browser, search_projects):

    search_url = search_projects.search_for(DEFAULT_PROJECT_NAME).current_url

    assert search_url == SITE_BASE_URL + SEARCH_PATH + DEFAULT_PROJECT_NAME


@pytest.fixture()
def search_results(browser):
    browser.get(SITE_BASE_URL + SEARCH_PATH + DEFAULT_PROJECT_NAME)
    return SearchResultsPage(browser)


def test_search_results_have_relevant_project_info(browser, search_results):

    project_name = search_results.get_first_project_name()
    project_url = search_results.get_first_project_url()
    assert DEFAULT_PROJECT_NAME.lower() in project_name.lower()
    assert project_url == SITE_BASE_URL + PROJECT_PATH + DEFAULT_PROJECT_NAME + "/"

# See test_project_url_opens_proper_project_page in project_test.py


