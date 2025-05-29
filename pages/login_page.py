from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.btn_submit = (By.CSS_SELECTOR, "button[type='submit']")


    def enter_username(self, username):
        wait = WebDriverWait(self.driver,20)
        wait.until(EC.presence_of_element_located((self.username))).send_keys(username)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((self.password))).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.btn_submit)
        ).click()


