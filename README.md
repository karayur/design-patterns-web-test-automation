(WIP) Design patterns, idioms, principles with web test automation examples in Python.

Inspired by [python-patterns](https://github.com/faif/python-patterns) and [Design patterns in test automation (in Russian)](https://habr.com/ru/company/jugru/blog/338836/)

Some notes and disclaimers:
* This doc and code examples were created as a part of my Python test automation learning project and it reflects my personal experience only (which isn’t very significant in Python though)
* Examples based on pypi.org web UI created for illustration purpose only. It isn't supposed anybody use a similar approach for test automation design of pypi.org or any other site with similar components / structure.
* As we know there is no such thing as a good design pattern or a bad design pattern. Each design pattern is created to address a specific problem or situation in development. If you don’t have such a problem do not use a pattern. Even though it is really cool.
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
- Ensure project url opens  appropriate project details
  - Open https://pypi.org/project/selenium/
  - Assert “Selenium” project header exists 

You may want to check if other projects in search results are relevant or check more details on the project page also. However, the main point is that you need more small tests. They start to look like unit tests and follow the Single Responsibility Principle more.

See code examples here:
- https://github.com/karayur/design-patterns-web-test-automation/blob/main/tests/search_test.py
- https://github.com/karayur/design-patterns-web-test-automation/blob/main/tests/project_test.py
  

# Page object pattern
## Overview
_Page objects are a classic example of encapsulation - they hide the details of the UI structure and widgetry from other components (the tests). _
[PageObject](https://martinfowler.com/bliki/PageObject.html) - Martin Fowler

_- The public methods represent the services that the page offers
- Try not to expose the internals of the page
- Generally don't make assertions
- Methods return other PageObjects
- Need not represent an entire page
- Different results for the same action are modelled as different methods_
Page Objects recommendations summary from https://github.com/SeleniumHQ/selenium/wiki/PageObjects

From the other hand ...
  _... However some practitioners prefer that page objects return some generic browser context, and the tests control which page objects to build on top of that context based on the flow of the test (particularly conditional flows). Their preference is based on the fact that the test script knows what pages are expected next and this knowledge doesn't need to be duplicated in the page objects themselves._
[PageObject](https://martinfowler.com/bliki/PageObject.html) - Martin Fowler

So choose your own approach
  
## Examples

Just for example I chose several Page Objects (you better think about them as panel objects or components) from pypi.org and group them in four groups
- Navigation - everything related to header and footer panels on almost every page 
- Project - related to progect description and navigation (e.g. https://pypi.org/project/selenium/).
- Search - everything related to search
- Login & Register - quite similar staf put at one file 

As a result I got next PagesObject files struture:
  
![unnamed (2)](https://user-images.githubusercontent.com/1383933/142002660-3f45b192-809d-4a74-8936-96781cfb2d2f.png)

See all pages here: https://github.com/karayur/design-patterns-web-test-automation/tree/main/pages
  
  
## Page object pattern and mixins
  
[Login](https://pypi.org/account/login/) and [Register](https://pypi.org/account/register/) pages have similar elements and behabior (password field, show password checkbox, usename field)
  
![Login](https://user-images.githubusercontent.com/1383933/142005912-194021cc-c63d-4e9b-ad59-f62de5d97322.png)
![Register](https://user-images.githubusercontent.com/1383933/142005932-77f81d1b-e1b4-4311-ab9e-32b516f3f6ba.png)

There are several ways to address it in a DRY way. 
Here example with mixin: 
  
https://github.com/karayur/design-patterns-web-test-automation/blob/main/pages/login_register.py

## the same mixins and structual subtyping using Protocol 
  
https://mypy.readthedocs.io/en/latest/more_types.html#mixin-classes

See eaxample (WIP)
https://github.com/karayur/design-patterns-web-test-automation/blob/main/pages/user_password_show_mixin.py  

# Page Element object pattern

## Overview
   
[Design patterns in test automation (in Russian)](https://habr.com/ru/company/jugru/blog/338836/)

  
## Examples
  
https://github.com/karayur/design-patterns-web-test-automation/blob/main/pages/page_elements.py
  
  
# Keeping ARRANGE phase in pytest fixtures 
  
## Overview

   _assert или exception в фикстуре приводит к ошибке (ERROR), в то время как assert или exception в тестовой функции приводит к ошибке (FAIL)._ 
  
https://habr.com/ru/post/448786/
  
## Example
  
Example with fixture
 
  https://github.com/karayur/design-patterns-web-test-automation/blob/main/tests/search_test.py
  
Example without fixture

  https://github.com/karayur/design-patterns-web-test-automation/blob/main/tests/project_test.py
  
  
  
