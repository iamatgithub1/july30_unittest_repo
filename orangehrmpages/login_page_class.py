from selenium import webdriver
from selenium.webdriver.common.by import By


class Hrm_Login_Pg:
    username = "username"
    password = "password"
    login_btn = '//form/div[3]/button'
    dashboard_header_locator = "h6"
    invalid_credential_locator = '//p[text()="Invalid credentials"]'
    logout_dd = "//p[@class='oxd-userdropdown-name']"
    logout_txt = "//a[text()='Logout']"

    def __init__(self, a_driver):
        self.my_driver = a_driver

    def enter_username(self, p_username):
        self.my_driver.find_element(By.NAME, self.username).send_keys(p_username)

    def enter_password(self, p_password):
        self.my_driver.find_element(By.NAME, self.password).send_keys(p_password)

    def login(self):
        self.my_driver.find_element(By.XPATH, self.login_btn).click()

    def logout(self):
        self.my_driver.find_element(By.XPATH, self.logout_dd).click()
        self.my_driver.find_element(By.XPATH, self.logout_txt).click()

    def verify_successful_login(self):
        dashboard_header_text = self.my_driver.find_element(By.TAG_NAME, self.dashboard_header_locator).text

        assert dashboard_header_text == "Dashboard"
        print(dashboard_header_text)

    def verify_unsuccessful_login_attempt(self):
        try:
            dashboard_header_text = self.my_driver.find_element(By.TAG_NAME, self.dashboard_header_locator).text
        except:
            print("In except block...")
            invalid_credentials_text = self.my_driver.find_element(By.XPATH, self.invalid_credential_locator).text
            print(invalid_credentials_text)
            assert invalid_credentials_text == "Invalid credentials"
