import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from page.main_page import MainPage


@pytest.fixture
def setup():
    chromedriver_autoinstaller.install()
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    driver.implicitly_wait(10)
    return driver


# Verifying that ebay home page is available and loads correctly by reading the categories
def test_home_available(setup):
    page = MainPage(setup)
    expected_categories = ['Luxury', 'Sneakers', 'P&A', 'Refurbished', 'Trading cards', 'Pre-loved Luxury', 'Toys']
    actual_categories = []

    cat_elements = page.find_elements('categories')

    for element in cat_elements:
        category_text = page.read_text(element)
        actual_categories.append(category_text)

    assert actual_categories == expected_categories


# Verifying that results are visible by reading the names of each item
def test_search(setup):
    page = MainPage(setup)
    results_text = []

    search_bar_element = page.find_element('search_bar')
    search_bar_element.send_keys('laptop')

    search_button_element = page.find_element('search_button')
    search_button_element.click()

    results_elements = page.find_elements('results')

    for result in results_elements:
        text = page.read_text(result)
        results_text.append(text)
        if len(results_text) > 0:
            assert True
            break
        else:
            assert False


# Testing that there are at least 10 results with the expected word.
def test_search_results(setup):
    page = MainPage(setup)
    results_text = []
    expected_word = 'laptop'

    search_bar_element = page.find_element('search_bar')
    search_bar_element.send_keys('laptop')

    search_button_element = page.find_element('search_button')
    search_button_element.click()

    results_elements = page.find_elements('results')

    for result in results_elements:
        text = page.read_text(result)
        if expected_word in text.lower():
            results_text.append(text)

    assert len(results_text) >= 10


# verifying that results has the expected word and there are al least 10 items as results
def test_search_results_include_term(setup):
    page = MainPage(setup)
    expected_word = 'laptop'

    search_bar_element = page.find_element('search_bar')
    search_bar_element.send_keys('laptop')

    search_button_element = page.find_element('search_button')
    search_button_element.click()

    results_elements = page.find_elements('results')

    assert len(results_elements) >= 10

    for result in results_elements:
        text = page.read_text(result)
        assert expected_word in text.lower()
