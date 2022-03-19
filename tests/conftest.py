from pytest import fixture

from selenium import webdriver


# 'session' will create only one chrome_browser for all the tests
@fixture(scope='session')
def chrom_browser():
    browser = webdriver.Chrome('D:\webdriver\chromedriver.exe')
    yield browser

    # Teardown
    print("\n I am tearing down this browser")
