import pytest

from pages.login_register import Login
from pages.login_register import Register
from tests.test_data import *

# login fixture параметризовать ?

urls = (
    SITE_BASE_URL + LOGIN_PAGE_PATH,
    SITE_BASE_URL + REGISTER_PAGE_PATH
)


# --------  Login form testing
@pytest.fixture()
def login(browser):
    browser.get(SITE_BASE_URL + LOGIN_PAGE_PATH)
    return Login(browser)


def test_login_password_hidden_by_default(browser, login):

    assert login.is_password_masked() is True


def test_login_switch_password_visibility(browser, login):

    login.toggle_show_password()

    assert login.is_password_masked() is False


# def test_login_with_correct_username_and_password()
# def test_login_with_incorrect_username_or_password()
# ...

# -------- Register form testing
@pytest.fixture()
def register(browser):
    browser.get(SITE_BASE_URL + REGISTER_PAGE_PATH)
    return Register(browser)


def test_register_password_hidden_by_default(browser, register):

    assert register.is_password_masked() is True
    assert register.is_confirm_password_masked() is True


def test_register_switch_password_visibility(browser, register):

    register.toggle_show_password()

    assert register.is_password_masked() is False
    assert register.is_confirm_password_masked() is False
