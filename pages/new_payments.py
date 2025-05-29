from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewPayments:
    def __init__(self, driver):
        self.driver = driver

        self.choose_inn = (By.CSS_SELECTOR,"body > div.v-overlay-container > div.v-overlay.v-overlay--active.v-theme--light.v-locale--is-ltr.v-dialog.v-dialog--fullscreen.custom-fullscreen-overflow-x.v-overlay--scroll-blocked > div > div > div.v-container.v-locale--is-ltr.h-100 > section > div > div > div.v-card.v-theme--light.v-card--density-default.v-card--variant-outlined > div.v-card-text > div > div > div.v-window-item.v-window-item--active > form > div > div:nth-child(2) > div > div.v-card-text.pa-0 > div > div:nth-child(1) > div > div > div > div > div.v-input__control > div > div.v-field__append-inner > button > span.v-btn__content > svg")
        self.choose_firm = (By.CSS_SELECTOR,"body > div.v-overlay-container > div:nth-child(84) > div.v-overlay__content > div > div > div.v-card-text.organization-v-text > div > div:nth-child(1) > div.v-row > div > div > div:nth-child(2) > div > div.v-table.v-table--has-top.v-table--has-bottom.v-table--hover.v-theme--light.v-table--density-default.v-data-table.text-no-wrap.custom-data-table.text-wrap.balance-padding-first-child-table > div > table > tbody > tr:nth-child(1) > td:nth-child(3)")
        self.money = (By.CSS_SELECTOR,"body > div.v-overlay-container > div.v-overlay.v-overlay--active.v-theme--light.v-locale--is-ltr.v-dialog.v-dialog--fullscreen.custom-fullscreen-overflow-x > div > div > div.v-container.v-locale--is-ltr.h-100 > section > div > div > div.v-card.v-theme--light.v-card--density-default.v-card--variant-outlined > div.v-card-text > div > div > div.v-window-item.v-window-item--active > form > div > div:nth-child(2) > div > div.v-card-text.pa-0 > div > div:nth-child(5) > span > div > div")
        self.dropdown_code = (By.CSS_SELECTOR,"body > div.v-overlay-container > div.v-overlay.v-overlay--active.v-theme--light.v-locale--is-ltr.v-dialog.v-dialog--fullscreen.custom-fullscreen-overflow-x > div > div > div.v-container.v-locale--is-ltr.h-100 > section > div > div > div.v-card.v-theme--light.v-card--density-default.v-card--variant-outlined > div.v-card-text > div > div > div.v-window-item.v-window-item--active > form > div > div:nth-child(3) > div > div.v-card-text.pa-0 > div > div:nth-child(1) > div > div > div > div > div.v-field__append-inner > svg")
        self.choose_code = (By.CSS_SELECTOR, "#v-menu-6880 > div > div > div:nth-child(3) > div  ")
        self.appoint = (By.ID,"body > div.v-overlay-container > div.v-overlay.v-overlay--active.v-theme--light.v-locale--is-ltr.v-dialog.v-dialog--fullscreen.custom-fullscreen-overflow-x.v-overlay--scroll-blocked > div > div > div.v-container.v-locale--is-ltr.h-100 > section > div > div > div.v-card.v-theme--light.v-card--density-default.v-card--variant-outlined > div.v-card-text > div > div > div.v-window-item.v-window-item--active > form > div > div:nth-child(3) > div > div.v-card-text.pa-0 > div > div:nth-child(2) > div")
        self.cancel = (By.CSS_SELECTOR,"body > div.v-overlay-container > div.v-overlay.v-overlay--active.v-theme--light.v-locale--is-ltr.v-dialog.v-dialog--fullscreen.custom-fullscreen-overflow-x.v-overlay--scroll-blocked > div > div > div.v-container.v-locale--is-ltr.h-100 > section > div > div > div.d-flex.mt-6.gap-3 > button:nth-child(1)")

    def click_choose_inn(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.choose_inn)
        ).click()

    def click_choose_firm(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.choose_firm)
        ).click()


    def enter_money(self,money):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.money)).send_keys(money)


    def click_dropdown_code (self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.dropdown_code)
        ).click()

    def click_choose_code (self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.choose_code)
        ).click()

    def enter_appoint(self,appoint):
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(self.appoint)).send_keys(appoint)

    def click_cancel(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.cancel)
        ).click()





