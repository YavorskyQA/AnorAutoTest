from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SelectFirms:
    def __init__(self, driver):
        self.driver = driver

        self.exit = (By.CSS_SELECTOR, "body > div.v-overlay-container > div > div.v-overlay__content > div > div.v-card-text > div.mt-4 > button")
        self.firm = (By.CSS_SELECTOR, "body > div.v-overlay-container > div > div.v-overlay__content > div > div.v-card-text > div.v-input.v-input--horizontal.v-input--center-affix.v-input--density-comfortable.v-theme--light.v-locale--is-ltr.v-radio-group > div > div > div > div.v-list.v-theme--light.v-list--density-comfortable.v-list--one-line.card-list > div:nth-child(1)")




    def click_exit(self):
        WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.exit)
            ).click()

    def click_firm(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.firm)
        ).click()
