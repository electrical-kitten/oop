from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time

test_info = ['Банный комплекс', 'мурино', 'Гражданка']
# @pytest.mark.parametrize()

def test_person_phone_filter(driver, user_info):
    wait = WebDriverWait(driver, timeout=5)
    login_input = driver.find_element(
        By.XPATH, '//input[@name="control-input-login"]')
    login_input.send_keys(user_info['users'][0]['user_login'])

    pass_input = driver.find_element(
        By.XPATH, '//input[@name="control-input-password"]')
    pass_input.send_keys(user_info['users'][0]['user_password'])

    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    persons_reg_icon = driver.find_element(
        By.XPATH, '//a[@name="NPersonInfo/registry"]')
    persons_reg_icon.click()

    filter_phone_btn = driver.find_element(
        By.XPATH, '//fck-field-button-overlay[@testid="phone"]')
    filter_phone_btn.click()

    filter_phone_input = driver.find_element(
        By. XPATH, '//input[@testid="phone"]')
    time.sleep(1)
    filter_phone_input.send_keys(user_info['users'][0]['user_login'])
 
    apply_btn = driver.find_element(
        By.XPATH, '//button[@class="m primary ng-star-inserted"] ')
    apply_btn.click()

    time.sleep(2)
    found_element = driver.find_element(
        By. XPATH, '//a[@class="link"]')
    link = found_element.get_attribute('href')

    try:
        assert user_info['users'][0]['person_info_id'] in link
    except:
        raise AssertionError(
            f"\n{user_info['person_info_id']} is not in {link}")


# def test_person_project_filter(driver, user_info):

#     login_input = driver.find_element(
#         By.XPATH, '//input[@name="control-input-login"]')
#     login_input.send_keys(user_info['users'][0]['user_login'])

#     pass_input = driver.find_element(
#         By.XPATH, '//input[@name="control-input-password"]')
#     pass_input.send_keys(user_info['users'][0]['user_password'])

#     login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
#     login_button.click()

#     persons_reg_icon = driver.find_element(
#         By.XPATH, '//a[@name="NPersonInfo/registry"]')
#     persons_reg_icon.click()

#     all_filters = driver.find_element(
#         # By.XPATH, '/html/body/app-root/app-template-module/app-personinfo-registry/div/div[2]/fck-registry-ui/fck-registry-v2/fck-registry-wrapper/div[1]/fck-registry-filter/div/div[2]/div/button')
#         By.XPATH, '//div[@class="content" and text()="Все фильтры"]/ancestor::button[@type="button"]')
#     all_filters.click()

#     project_filter = driver.find_element(
#         By.XPATH, '//p[text()=" Проект "]/ancestor::button[@class="accordion_heading"]')
#     project_filter.click()

#     project_search = driver.find_element(By.XPATH, '//input[@testid="Поиск"]')
#     project_search.click()
#     project_search.send_keys(test_info[0])

#     prj_for_vlad = driver.find_element(
#         By.XPATH, '//div[@class="button_content" and text()=" Банный комплекс "]/ancestor::div[@class="button"]')
#     prj_for_vlad.click()

#     project_search.clear()
#     project_search.send_keys(test_info[1])

#     prj_for_polya = driver.find_element(
#         By.XPATH, '//div[@class="button_content" and text()=" мурино "]/ancestor::div[@class="button"]')
#     prj_for_polya.click()

#     project_search.clear()
#     project_search.send_keys(test_info[2])

#     prj_for_yulya = driver.find_element(
#         By.XPATH, '//div[@class="button_content" and text()=" Гражданка "]/ancestor::div[@class="button"]')
#     prj_for_yulya.click()
#     time.sleep(1)

#     apply_btn = driver.find_element(
#         By.XPATH, '//button[@class="l primary ng-star-inserted"]')
#     apply_btn.click()
#     time.sleep(2)


@pytest.mark.garbage
def test_two():
    assert 2 == 2
