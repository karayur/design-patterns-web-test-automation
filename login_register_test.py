import pytest

from utils.urls import SITE_BASE_URL
from pages.project.project_header import ProjectHeader
from pages.search.search_projects import Search4Projects
from pages.search.search_results import SearchResults


@pytest.fixture()
def search_results(browser):
    browser.get(SITE_BASE_URL + "search/?q=selenium")
    return SearchResults(browser)


@pytest.fixture()
def search4projects(browser):
    browser.get(SITE_BASE_URL)
    return Search4Projects(browser)


def test_show_password_option(browser):
    search4projects.enter_search_keyword("selenium")  # TODO remove hardcoded string

    # TODO probably think about other way te test than items count
    projects_count = SearchResults(browser) \
        .get_projects_count()
    assert projects_count >= 20  # TODO remove hardcoded number


def test_open_project_from_search_results(browser, search_results):
    search_results.click_on_first_item()

    project_name = ProjectHeader(browser) \
        .get_project_name()
    assert len(project_name.strip()) > 0  # asset project name isn't blank
