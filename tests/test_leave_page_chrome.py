import json
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from orangehrmpages.leave_page_class import HrmLeavePg
from orangehrmpages.login_page_class import Hrm_Login_Pg
from utilities.org_hrm_helper import org_hrm_logout
from utilities.util import check_for_title, take_screenshot
from os.path import dirname as up

class LoginPgTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:

        cwd = os.getcwd()
        cwd_one_up = up(up(__file__))
        json_file_path = cwd_one_up + "\\data_source\\org_hrm_test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)
        print(cls.data_dict.get("login_credentials").get("correct_username"))
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # time.sleep(60)

    def test_org_hrm_approve_leave_successful(self):
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_project.enter_password("admin123")
        hrm_project.login()
        hrm_project.verify_successful_login()
        self.driver.get_screenshot_as_png()

        hrm_leave = HrmLeavePg(self.driver)
        hrm_leave.navigate_to_leave_page()
        take_screenshot(self.driver)

        hrm_leave.verify_dates()
        take_screenshot(self.driver)
        hrm_leave.scroll_to_results()
        take_screenshot(self.driver)



