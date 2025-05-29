from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

        self.drop_down_select_firm = (By.CSS_SELECTOR,"#app > div > div > div > div > div > div:nth-child(1) > div > div > div > div > div.me-1 > button")
        self.choose_firm = (By.CSS_SELECTOR,"#v-menu-19 > div > div > div:nth-child(7)")
        self.new_payment = (By.CSS_SELECTOR,"#app > div > div > div > div > div > div:nth-child(2) > main > div:nth-child(1) > div > div.v-card.v-theme--light.v-card--density-default.v-card--variant-elevated.d-flex.mb-6.pa-5 > div.d-flex.gap-3.align-center.pr-1 > div:nth-child(2) > button")
        self.payment_order = (By.CSS_SELECTOR,"body > div.v-overlay-container > div.v-overlay.v-overlay--active.v-theme--light.v-locale--is-ltr.v-dialog.v-overlay--scroll-blocked > div.v-overlay__content > div > div.v-list.v-theme--light.v-list--density-comfortable.v-list--one-line > div:nth-child(2)")


    def click_drop_down_select_firm(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.drop_down_select_firm)
        ).click()

    def click_choose_firm(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.choose_firm)
        ).click()

    def click_new_payment(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_payment)
        ).click()

    def click_payment_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.payment_order)
        ).click()



