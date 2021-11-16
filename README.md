(WIP) Design patterns, idioms, principles with web test automation examples in Python.

Inspired by [python-patterns](https://github.com/faif/python-patterns) and [Design patterns in test automation (in Russian)](https://habr.com/ru/company/jugru/blog/338836/)

Some notes and disclaimers:
* This doc and code examples were created as a part of my Python test automation learning project. It reflects my personal experience which isn’t very significant (at least in Python).
* Examples based on pypi.org web UI created for illustration purpose only. It isn't supposed anybody use a similar approach for test automation design of pypi.org or any other site with similar components / structure.
* There is no such thing as a good design pattern or a bad design pattern. Each design pattern is created to address a specific problem or situation in development. If you don’t have such a problem do not use a pattern. Even though it is really cool.
* You might not need most of these patterns in end-to-end test automation. Even if you have a quite big system you better concentrate on unit and integration levels of [testing pyramid](url) (if it is possible). In this case the end-to-end test automation pack and framework is gonna be lightweight. 

# Atomic automated test approach

## Overview
_An automated atomic test (AAT) is one that tests only a single feature or component. AAT have very few UI interactions and typically touch a maximum of two screens. The “typical” UI end-to-end tests break the AAT pattern._

_AATs meet several requirements of good tests as specified by Kent Beck
Isolated
Composable
Fast_
[Top 17 Automated Testing Best Practices (Supported By Data)](https://ultimateqa.com/automation-patterns-antipatterns#Best_Practice_Tests_Should_Be_Atomic) - Nikolay Advolodkin 

To achieve it you may want to even test your UI components directly 

_Unlike end-to-end tests, tests for individual UI components don’t require a backend server or the entire app to be rendered. Instead, these  tests run in the same self-contained environment and take a similar amount of time to execute as unit tests that just execute the underlying event handlers directly_
[Google Testing Blog: Testing on the Toilet: Testing UI Logic? Follow the User!](https://testing.googleblog.com/2020/10/testing-on-toilet-testing-ui-logic.html) - Carlos Israel Ortiz García

## Examples

Consider testing project search functionality in https://pypi.org  (lets assume that creating unit or/and integration tests is much costly for whatever reasons).

Traditional E2E test may looks like
Open https://pypi.org
- Search for “Selenium”
- Assert it is the first project in the list on search result page
- Click on it
- Assert “Selenium” project details exist 

Following AAT approach we need to create three tests at least:
- Ensure search for “Selenium” opens appropriate search url
  - Open https://pypi.org
  - Search for “selenium”
  - assert appropriate search url opens (i.e. https://pypi.org/search/?q=selenium)
- Ensure search results has “selenium” project as the first item 
  - Open https://pypi.org/search/?q=selenium, 
  - Assert Selenium is the first project in the search result
  - Assert proper href to selenium project is exist (i.e. https://pypi.org/project/selenium/)
    - Any <a> tag in HTML is clickable you don’t need to test it by real clicking
- Ensure “selenium” project has appropriate name in header
  - Open https://pypi.org/project/selenium/
  - Assert “Selenium” project header exists 

You may want to check if other projects in search results are relevant or check more details on the project page also. However, the main point is that you need more small tests. They start to look like unit tests and follow the Single Responsibility Principle more.

https://github.com/karayur/design-patterns-web-test-automation/blob/def2ef9225018f0dc5ca0d34b68a4ebb6fe21bc8/tests/search_test.py#L8-L18
  
