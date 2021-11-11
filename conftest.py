import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")  # TODO clarify if we can use autouse="true" here
def browser():
    # s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver.get(SITE_BASE_URL)
    yield driver
    driver.quit()



# @pytest.fixture(scope="function")
# def setup(browser):
#     browser.get(BasePage)
