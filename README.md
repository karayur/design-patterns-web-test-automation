**Design patterns, idioms, principles with web test automation examples in Python.**

The idea is to have popular patterns gathered not as standalone python code examples but all integrated in one project that is really testing some webui.

Inspired by: 
* https://github.com/faif/python-patterns
* [Design Patterns for High-Quality Automated Tests: High-Quality Test Attributes and Best Practices](https://www.amazon.com/gp/product/B085L9W1KH/ref=ppx_yo_dt_b_d_asin_title_o00?ie=UTF8&psc=1)
* [Design patterns in test automation (in Russian)](https://habr.com/ru/company/jugru/blog/338836/)


Some notes and disclaimers:
* This doc and code examples were created as a part of my Python test automation learning project and it reflects my personal experience only (which isn’t very significant in Python though)
* Examples based on pypi.org web UI created for illustration purpose only. It isn't supposed anybody use a similar approach for test automation design of pypi.org or any other site with similar components / structure.
* As we know there is no such thing as a good design pattern or a bad design pattern. Each design pattern is created to address a specific problem or situation in development. If you don’t have such a problem do not use a pattern. Even though it is really cool.
* You might not need most of these patterns in end-to-end test automation. Even if you have a quite big system you better concentrate on unit and integration levels of [testing pyramid](url) (if it is possible). In this case the end-to-end test automation pack and framework is gonna be lightweight. However exception are possible (at least I've seen some).

See details on wiki pages:
 * [Automated atomic tests approach](https://github.com/karayur/design-patterns-web-test-automation/wiki/Automated-atomic-tests-approach) 
 * [Page object pattern](https://github.com/karayur/design-patterns-web-test-automation/wiki/Page-object-pattern)
    * page objects modules structure
    * mixins to page objects 
    * mixins and structual subtyping using Protocol (WIP)
 * [Page element pattern (WIP)](https://github.com/karayur/design-patterns-web-test-automation/wiki/Page-element-pattern)
 * [Value Object pattern (WIP)](https://github.com/karayur/design-patterns-web-test-automation/wiki/Value-Object-pattern)
 * [Pytest fixtures and ARRANGE step in tests (WIP)](https://github.com/karayur/design-patterns-web-test-automation/wiki/Pytest-fixtures-and-ARRANGE--step-in-tests)
  
