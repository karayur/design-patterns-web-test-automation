import pytest

from pages.login_register.login import Login
from pages.login_register.register import Register
from utils.test_data import *

# login fixture параметризовать ?

urls = (
    SITE_BASE_URL + LOGIN_PAGE_PATH,
    SITE_BASE_URL + REGISTER_PAGE_PATH
)


# -------- Testing Login form
@pytest.fixture()
def login(browser):
    browser.get(SITE_BASE_URL + LOGIN_PAGE_PATH)
    return Login(browser)


def test_login_password_hidden_by_default(browser, login):
    login.enter_password(DEFAULT_PASSWORD)  # not necessary here

    assert login.is_password_masked() is True


def test_login_switch_password_visibility(browser, login):
    login.enter_password(DEFAULT_PASSWORD)  # not necessary here
    login.toggle_show_password()

    assert login.is_password_masked() is False


# def test_login_with_correct_username_and_password()
# def test_login_with_incorrect_username_or_password()
# ...

# -------- Testing Register form
@pytest.fixture()
def register(browser):
    browser.get(SITE_BASE_URL + REGISTER_PAGE_PATH)
    return Register(browser)


def test_register_password_hidden_by_default(browser, register):
    register.enter_password(DEFAULT_PASSWORD)  # not so necessary here
    register.enter_password(DEFAULT_PASSWORD)

    assert register.is_password_masked() is True
    assert register.is_password_confirm_masked() is True


def test_register_switch_password_visibility(browser, register):
    register.enter_password(DEFAULT_PASSWORD)  # not so necessary here
    register.enter_password(DEFAULT_PASSWORD)
    register.toggle_show_password()

    assert register.is_password_masked() is False
    assert register.is_password_confirm_masked() is False
