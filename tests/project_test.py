import pytest

from tests.test_data import *
from pages.project.project_header import ProjectHeaderPage


def test_project_url_opens_proper_project_page(browser):
    # ARRANGE without fixture example
    browser.get(SITE_BASE_URL + PROJECT_PATH + DEFAULT_PROJECT_NAME)
    project_header = ProjectHeaderPage(browser)

    project_name = project_header.get_project_name()
    assert project_name.startswith(DEFAULT_PROJECT_NAME)
