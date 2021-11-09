import pytest

from utils.urls import *
from pages.project.project_header import ProjectHeader
from pages.search.search_projects import Search4Projects
from pages.search.search_results import SearchResults


@pytest.fixture()
def search4projects(browser):
    browser.get(SITE_BASE_URL)
    return Search4Projects(browser)


def test_search_returns_projects_list(browser, search4projects):
    search4projects.search_for_keyword(DEFAULT_PROJECT_NAME)  # using fixture for ARRANGE

    projects_count = SearchResults(browser) \
        .get_projects_count()
    assert projects_count >= MAX_COUNT_PROJECTS_IN_SEARCH_RESULT


def test_search_redirect_to_proper_search_url(browser):
    browser.get(SITE_BASE_URL)  # NOT using fixture for ARRANGE
    search4projects = Search4Projects(browser)

    search4projects.search_for_keyword(DEFAULT_PROJECT_NAME)

    search_url = browser.current_url
    assert search_url == SITE_BASE_URL + SEARCH_PATH + DEFAULT_PROJECT_NAME


@pytest.fixture()
def search_results(browser):
    browser.get(SITE_BASE_URL + SEARCH_PATH + DEFAULT_PROJECT_NAME)
    return SearchResults(browser)


def test_open_project_from_search_results(browser, search_results):
    search_results.click_on_first_item()

    project_name = ProjectHeader(browser) \
        .get_project_name()
    assert len(project_name.strip()) > 0  # asset project name isn't blank
