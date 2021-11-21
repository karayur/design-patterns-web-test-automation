from pages.search.search_projects import SearchProjectsPage


def test_search_open_proper_search_url(browser):
    # ARRANGE
    browser.get("https://pypi.org/")
    search_for_projects = SearchProjectsPage(browser)

    # ACT
    search_for_projects.search_for("selenium")

    # ASSERT
    search_url = browser.current_url
    assert search_url == "https://pypi.org/search/?q=selenium"



from typing import Protocol


class HasValueProtocol(Protocol):
    @property
    def value(self) -> int: ...


class MultiplicationMixin:

    def multiply(self: HasValueProtocol, m: int) -> int:
        return self.value * m


class AdditionMixin:

    def add(self: HasValueProtocol, b: int) -> int:
        return self.value + b


class MyClass(MultiplicationMixin, AdditionMixin):
    def __init__(self, value: int) -> None:
        self.value2 = value


instance = MyClass(10)
print(instance.add(2))
print(instance.multiply(2))
