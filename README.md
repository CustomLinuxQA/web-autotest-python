Доброго дня.
## Команды для запуска тестов:
pytest -v -s --language=ru test/test_product_page.py --alluredir=allure-report

pytest -v -s --language=ru test/test_product_page.py::TestGuestFromProductPage::test_guest_can_add_product_to_basket --alluredir=allure-report

pytest -v --tb=line --language=en -m need_review

16 проверок.


Так же прописал:
#### conftest.py:
--browser_name=chrome
--language=en
#### pytest.ini:
--reruns=2

## Что будет доработано:
- in progress

Хорошего дня.
