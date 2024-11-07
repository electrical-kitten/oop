from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import pyautogui


def test_attach_photo(driver, user_info):
    login_input = driver.find_element(
        By.XPATH, '//input[@name="control-input-login"]')
    login_input.send_keys(user_info['users'][0]['user_login'])

    pass_input = driver.find_element(
        By.XPATH, '//input[@name="control-input-password"]')
    pass_input.send_keys(user_info['users'][0]['user_password'])

    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()

    time.sleep(3)

    create_goods = driver.find_element(By.XPATH, '/html/body/app-root/app-template-module/header/div/div/div/div/div[1]/button[1]')
    create_goods.click()

    time.sleep(3)

    # attach_photo = driver.find_element(By.XPATH, '//upload-photo[@class="ng-star-inserted"]')
    # attach_photo.click()
    # time.sleep(3)

    # pyautogui.write('attach_test.jpg') 
    # # time.sleep(3)
    # pyautogui.press('enter')

    # time.sleep(2)

    goods_name_input = driver.find_element(By.XPATH, '//textarea[@id="mat-input-23"]')
    goods_name_input = driver.find_element(By.XPATH, '/html/body/app-root/app-template-module/app-goods-editor/div/div/div[1]/field-render-module/div/controls-render/div/div/div[2]/control-string/field-template/div/div[2]/div/textarea')
    goods_name_input.click()
    goods_name_input.send_keys('attach photo autotest')

    goods_category_btn = driver.find_element(By.XPATH, '/html/body/app-root/app-template-module/app-goods-editor/div/div/div[1]/field-render-module/div/controls-render/div/div/div[5]/select-category-control/field-template/div/div[2]/button')
    goods_category_btn.click()


    goods_category_element = driver.find_element(By.XPATH, '//*[text()="бытовой инструмент"]/ancestor::button')
    goods_category_element.click()

    goods_category_apply  = driver.find_element(By.XPATH, '//button[text()="Применить"]')
    goods_category_apply.click()

    goods_save_btn = driver.find_element(By.XPATH, '//button[text()="Сохранить"]')
    goods_save_btn.click()
    time.sleep(3)

    goods_id = driver.find_element(By.XPATH, '//div[@class="id ng-star-inserted"]')
    found_id = goods_id.text
    print(found_id)
    
    # try:
    #     assert 'attach_test.jpg' in driver.page_source
    # except:
    #     assert False



