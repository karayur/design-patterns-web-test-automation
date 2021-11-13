from typing import NamedTuple

SITE_BASE_URL = "https://pypi.org/"
SEARCH_PATH = "search/?q="
LOGIN_PAGE_PATH = "account/login/"
REGISTER_PAGE_PATH = "account/register/"
DEFAULT_PASSWORD = "!@#$%^&*()12Qw"
DEFAULT_PROJECT_NAME = "selenium"
LIGHT_PROJECT_NAME = "bnbad2"
MAX_COUNT_PROJECTS_IN_SEARCH_RESULT = 20


# DEFAULT_USER_AND_PASSWORD =

class UsernameAndPassword(NamedTuple):
    username: str
    password: str


class UserCredentials(NamedTuple):
    name: str
    email: str
