import pytest
import json
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get('https://multishik.cynteka.ru')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    # print('end of tests')


@pytest.fixture(scope='session')
def all_tests():
    print('\nТест русского')
    yield
    print('\nafter all')


@pytest.fixture()
def user_info():
    # file = open('./g/user_info.json', encoding='utf-8')
    file = open('./user_info.json', encoding='utf-8')
    user_info = json.load(file)

    return user_info
