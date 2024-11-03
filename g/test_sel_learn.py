from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.mark.parametrize()
def test_fk_login(driver, user_info):
    login_input = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/div[1]/control/app-control-input-phone/app-control-input/input')
    pass_input = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/div[2]/control/app-control-input-password/app-control-input/input')
    login_button = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/app-login/div/div[1]/form/button')

    login_input.click()
    login_input.send_keys(user_info['user_login'])
    pass_input.send_keys(user_info['user_password'])
    login_button.click()

    menu_btn = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/header/div/div/button')
    menu_btn.click()

    persons_reg_icon = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/side-navigation/div[1]/div/div[1]/a/div[2]/div')
    persons_reg_icon.click()

    phone_button = driver.find_element(
        By.XPATH, '/html/body/app-root/app-template-module/app-personinfo-registry/div/div[2]/fck-registry-ui/fck-registry-v2/fck-registry-wrapper/div[1]/fck-registry-filter/div/div[2]/div/fck-field-button-overlay[3]/fck-field-render/fck-text-field-button/span/button')
    phone_button.click()

    filter_phone_input = driver.find_element(By. XPATH, '//input[@type="tel"]')
    filter_phone_input.click()
    # time.sleep(2)
    filter_phone_input.send_keys(user_info['user_login'])
    # time.sleep(2)

    apply_btn = driver.find_element(
        By.XPATH, '//button[@class="l primary ng-star-inserted"]')
    apply_btn.click()

    time.sleep(1)
    found_element = driver.find_element(
        By. XPATH, '//a[@class="link"]')
    link = found_element.get_attribute('href')

    try:
        assert user_info['person_info'] in link
    except:
        raise AssertionError(
            f"\n{user_info['person_info']} is not in {link}")


@pytest.mark.garbage
def test_one(user_info):
    print(user_info["f_name"])
    assert 1 == 1


@pytest.mark.garbage
def test_two():
    assert 2 == 2
