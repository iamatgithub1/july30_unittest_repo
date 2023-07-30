import json
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from orangehrmpages.login_page_class import Hrm_Login_Pg
from utilities.org_hrm_helper import org_hrm_logout
from utilities.util import check_for_title


class LoginPgTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:

        cwd = os.getcwd()
        json_file_path = cwd + "\\data_source\\org_hrm_test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)
        print(cls.data_dict.get("login_credentials").get("correct_username"))
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # time.sleep(60)

    def test_org_hrm_login_unsuccessful(self):
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("incorrect_username"))
        hrm_project.enter_password("admin123")
        hrm_project.login()
        hrm_project.verify_unsuccessful_login_attempt()

    def test_org_hrm_login_successfully(self):
        print(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_project.enter_password(self.data_dict.get("login_credentials").get("correct_password"))
        hrm_project.login()
        check_for_title(self.driver, "Dashboard")
        org_hrm_logout(self.driver)
        # hrm_project.logout()

    # def tearDown(self) -> None:
    #     self.driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click()
    #     logout_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']")))
    #     logout_btn.click()
