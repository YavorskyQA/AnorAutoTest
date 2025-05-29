import time

import pytest
from pages.login_page import LoginPage
from pages.select_firms import SelectFirms
from pages.main_page import MainPage
from pages.new_payments import NewPayments

def test_login_succes(driver):
    driver.get("https://auth-staging.anorbank.uz/")

    login = LoginPage(driver)
    login.enter_username("micros24")
    login.enter_password("Micros24_pass_new")
    login.click_login()
    time.sleep(2)


    select_firms = SelectFirms(driver)
    select_firms.click_exit()
    time.sleep(2)

    login.enter_username("micros24")
    login.enter_password("Micros24_pass_new")
    login.click_login()
    time.sleep(2)

    select_firms = SelectFirms(driver)
    select_firms.click_firm()
    time.sleep(2)

    main_page = MainPage(driver)
    main_page.click_drop_down_select_firm()
    main_page.click_choose_firm()
    main_page.click_new_payment()
    main_page.click_payment_order()

    new_payments = NewPayments(driver)
    new_payments.click_choose_inn()
    new_payments.click_choose_firm()
    time.sleep(2)
    #new_payments.enter_money("123")
    #new_payments.click_dropdown_code()
    #time.sleep(4)
    #new_payments.click_choose_code()
    #new_payments.enter_appoint("TESTTEXT")
    new_payments.click_cancel()

