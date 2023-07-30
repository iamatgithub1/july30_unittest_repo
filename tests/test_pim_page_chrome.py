import json
import os
import time
import unittest
from os.path import dirname as up
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from orangehrmpages.login_page_class import Hrm_Login_Pg
from orangehrmpages.pim_page_class import HRM_PIM_Page
from utilities.org_hrm_helper import org_hrm_logout
from utilities.util import check_for_title, take_screenshot


class PIMPgTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        cwd = os.getcwd()
        cwd_one_up = up(up(__file__))
        json_file_path =  cwd_one_up + "\\data_source\\org_hrm_test_data.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # time.sleep(60)

    def test_add_employee_successful(self):
        hrm_project = Hrm_Login_Pg(self.driver)
        hrm_project.enter_username(self.data_dict.get("login_credentials").get("correct_username"))
        hrm_project.enter_password(self.data_dict.get("login_credentials").get("correct_password"))
        hrm_project.login()
        check_for_title(self.driver, "Dashboard")

        hrm_pim_obj = HRM_PIM_Page(self.driver)
        hrm_pim_obj.navigate_to_pim_module()
        hrm_pim_obj.add_employee(self.data_dict.get("employee_info").get("f_name"),
                                     self.data_dict.get("employee_info").get("m_name"),
                                     self.data_dict.get("employee_info").get("l_name"))
        time.sleep(10)
        take_screenshot(self.driver)
        hrm_pim_obj.verify_successful_addition_of_employee(self.data_dict.get("employee_info").get("f_name"), self.data_dict.get("employee_info").get("l_name"))
        take_screenshot(self.driver)
