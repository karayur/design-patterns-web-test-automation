import pytest

from pages.login_register.login import Login
from utils.test_data import *
from pages.project.project_header import ProjectHeader
from pages.search.search_projects import Search4Projects
from pages.search.search_results import SearchResults


# login fixture параметризовать ?


@pytest.fixture()
def login(browser):
    browser.get(SITE_BASE_URL + LOGIN_PAGE_PATH)
    return Login(browser)


def test_password_hidden_by_default(browser, login):
    login.enter_user_password(DEFAULT_PASSWORD)

    assert login.is_password_hidden() is True

# def test_user_can_switch_password_visibility(browser, login)
