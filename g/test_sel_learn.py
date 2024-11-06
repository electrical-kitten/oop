from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

test_info = ['Банный комплекс', 'мурино', 'Гражданка']

# @pytest.mark.parametrize()
def test_fk_login(driver, user_info):
    login_input = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/div[1]/control/app-control-input-phone/app-control-input/input')
    pass_input = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/div[2]/control/app-control-input-password/app-control-input/input')
    login_button = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/button')

    login_input.click()
    # login_input.send_keys(user_info['user_login'])
    login_input.send_keys(user_info['users'][0]['user_login'])
    pass_input.send_keys(user_info['users'][0]['user_password'])
    # pass_input.send_keys(user_info['user_password'])
    login_button.click()

    menu_btn = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/header/div/div/button')
    menu_btn.click()

    persons_reg_icon = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/side-navigation/div[1]/div/div[1]/a/div[2]/div')
    persons_reg_icon.click()

######### filter by phone number #########

    # phone_button = driver.find_element(
    #     # By.XPATH, '/html/body/app-root/app-template-module/app-personinfo-registry/div/div[2]/fck-registry-ui/fck-registry-v2/fck-registry-wrapper/div[1]/fck-registry-filter/div/div[2]/div/fck-field-button-overlay[3]/fck-field-render/fck-text-field-button/span/button')
    #     By.CSS_SELECTOR, 'fck-field-button-overlay[testId="phone"]')

    # phone_button.click()

    # filter_phone_input = driver.find_element(By. XPATH, '//input[@type="tel"]')
    # filter_phone_input.click()
    # # time.sleep(2)
    # filter_phone_input.send_keys(user_info['user_login'])
    # # time.sleep(2)

    # apply_btn = driver.find_element(
    #     By.XPATH, '//button[@class="l primary ng-star-inserted"]')
    # apply_btn.click()

    # time.sleep(1)
    # found_element = driver.find_element(
    #     By. XPATH, '//a[@class="link"]')
    # link = found_element.get_attribute('href')

    # try:
    #     assert user_info['person_info'] in link
    # except:
    #     raise AssertionError(
    #         f"\n{user_info['person_info']} is not in {link}")

######### filter by projects for Vlados #########

    all_filters = driver.find_element(By.XPATH, '/html/body/app-root/app-template-module/app-personinfo-registry/div/div[2]/fck-registry-ui/fck-registry-v2/fck-registry-wrapper/div[1]/fck-registry-filter/div/div[2]/div/button')

    all_filters.click()

    project_filter = driver.find_element(By.XPATH, '//p[text()=" Проект "]/ancestor::button[@class="accordion_heading"]')
    project_filter.click()


    project_search = driver.find_element(By.XPATH, '//input[@testid="Поиск"]')
    project_search.click()
    project_search.send_keys(test_info[0])

    prj_for_vlad = driver.find_element(By.XPATH, '//div[@class="button_content" and text()=" Банный комплекс "]/ancestor::div[@class="button"]')
    prj_for_vlad.click()

    project_search.clear()
    project_search.send_keys(test_info[1])

    prj_for_polya = driver.find_element(By.XPATH, '//div[@class="button_content" and text()=" мурино "]/ancestor::div[@class="button"]')
    prj_for_polya.click()

    project_search.clear()
    project_search.send_keys(test_info[2])


    prj_for_yulya = driver.find_element(By.XPATH, '//div[@class="button_content" and text()=" Гражданка "]/ancestor::div[@class="button"]')
    prj_for_yulya.click()
    time.sleep(1)


    apply_btn = driver.find_element(By.XPATH, '//button[@class="l primary ng-star-inserted"]')
    apply_btn.click()



@pytest.mark.garbage
def test_two():
    assert 2 == 2
