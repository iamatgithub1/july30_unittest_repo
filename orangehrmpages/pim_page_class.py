import subprocess
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from utilities.util import check_for_title, take_screenshot


class HRM_PIM_Page:
    element_pim_link = "//span[text()='PIM']"
    add_employee_btn = "//button[text()=' Add ']"
    emp_first_name = "firstName"
    emp_middle_name = "middleName"
    emp_last_name = "lastName"
    save_btn = "//button[text()=' Save ']"
    emp_id = 0
    emp_list = []
    pim_pg_tabs = "//a[@class='oxd-topbar-body-nav-tab-item']"
    pim_emp_total = "//div[@class='orangehrm-header-container']/following-sibling::div/div[1]/span"
    pim_search_results_table = "//*[@role='table']/div[2]/div"
    pim_search_results_table_emp_id=  "//div[@class='oxd-table-body']/div/div/div[2]/div"
    pim_emp_fname_search_input = "//input[@placeholder='Type for hints...'][1]"
    pim_search_table_rows= "//div[@class='oxd-table-card']"
    pim_add_img_btn = "//div[@class='employee-image-wrapper']//following-sibling::button"

    def __init__(self, a_driver):
        self.my_driver = a_driver
        self.my_driver.implicitly_wait(5)

    def auto_it_upload(self):
        script_path = "C:\\C Drive_GUVI_Lectures\\auto_id_exe\\Orange.exe"
        subprocess.run(script_path, shell=True)

    def navigate_to_pim_module(self):
        self.my_driver.find_element(By.XPATH, self.element_pim_link).click()
        check_for_title(self.my_driver, "PIM")

    def add_employee(self, f_name, m_name, l_name):
        print("I am in add employee page")
        self.my_driver.find_element(By.XPATH, self.add_employee_btn).click()
        self.my_driver.find_element(By.NAME, self.emp_first_name).send_keys(f_name)
        self.my_driver.find_element(By.NAME, self.emp_middle_name).send_keys(m_name)
        self.my_driver.find_element(By.NAME, self.emp_last_name).send_keys(l_name)
        self.my_driver.find_element(By.XPATH, self.pim_add_img_btn).click()
        time.sleep(5)
        self.auto_it_upload()
        time.sleep(5)
        self.my_driver.find_element(By.XPATH, self.save_btn).click()

    def verify_successful_addition_of_employee(self, f_name, l_name):
        # try:
        #     assert self.my_driver.find_element(By.XPATH, '//span[text()="Employee Id already exists"]')
        # except:
        name_check = f_name+' '+l_name
        assert self.my_driver.find_element(By.XPATH, f"//h6[text()='{name_check}']")
        assert self.my_driver.find_element(By.XPATH, '//label[text()="Employee Id"]')
        time.sleep(10)
        emp_id_label = self.my_driver.find_element(By.XPATH, '//label[text()="Employee Id"]')
        driver_license_label = self.my_driver.find_element(locate_with(By.TAG_NAME, "label").below(emp_id_label))

        print(
            self.my_driver.execute_script('return document.getElementsByClassName("oxd-input oxd-input--active")[1].value'))
        print(
            self.my_driver.execute_script('return document.getElementsByClassName("oxd-input oxd-input--active")[2].value'))
        print(
            self.my_driver.execute_script('return document.getElementsByClassName("oxd-input oxd-input--active")[3].value'))
        print(
            self.my_driver.execute_script('return document.getElementsByClassName("oxd-input oxd-input--active")[4].value'))
        print(
            self.my_driver.execute_script('return document.getElementsByClassName("oxd-input oxd-input--active")[5].value'))

        self.emp_id = self.my_driver.execute_script('return document.getElementsByClassName("oxd-input oxd-input--active")[5].value')
        self.employee_search(self.emp_id)
        return(self.emp_id)

    def employee_search(self, emp_id):
        pim_search_results_grid = self.my_driver.find_elements(By.XPATH, self.pim_search_results_table)
        print(len(pim_search_results_grid))

        element_add_employee = self.my_driver.find_elements(By.XPATH, self.pim_pg_tabs)
        element_add_employee[0].click()
        time.sleep(5)
        pim_employee_list_search = self.my_driver.find_element(By.XPATH,self.pim_emp_fname_search_input)
        # pim_employee_list_search.send_keys(f_name)
        pim_search_employee = self.my_driver.find_element(By.XPATH, "//button[@type='submit']")
        pim_search_employee.click()
        time.sleep(5)
        try:
            pim_search_results_grid_emp_id = self.my_driver.find_element(By.XPATH,
                                                                   self.pim_search_results_table_emp_id)
            print(len(pim_search_results_grid))
            # searched_emp_id = pim_search_results_grid_emp_id.text
            # print(searched_emp_id)
            # assert searched_emp_id == emp_id


            total_number_of_records_span_text = self.my_driver.find_element(By.XPATH, self.pim_emp_total )
            print(total_number_of_records_span_text.text)

            pim_search_results_grid_1_of_x_pages = self.my_driver.find_elements(By.XPATH,self.pim_search_table_rows )
            print(len(pim_search_results_grid_1_of_x_pages))
            try:
                for i in range(1, len(pim_search_results_grid_1_of_x_pages) + 1):
                    self.emp_list.append(self.my_driver.find_element(By.XPATH,
                                                                 f'//div[@class="oxd-table-card"][{i}]/div/div[2]/div').text)
                print(*self.emp_list)
            except Exception as e:
                print(e)

            for z in range(2, 100):
                try:
                    self.my_driver.find_element(By.XPATH,
                                                 f"//ul[@class='oxd-pagination__ul']/li[2]/button[text()={z}]").click()
                    total_number_of_records_span_text = self.my_driver.find_element(By.XPATH, self.pim_emp_total)
                    print(total_number_of_records_span_text.text)
                    pim_search_results_grid_1_of_x_pages = self.my_driver.find_elements(By.XPATH, self.pim_search_table_rows )

                    for i in range(1, len(pim_search_results_grid_1_of_x_pages) + 1):
                        self.emp_list.append(self.my_driver.find_element(By.XPATH,
                                                                     f'//div[@class="oxd-table-card"][{i}]/div/div[2]/div').text)
                    print(*self.emp_list)
                    take_screenshot(self.my_driver)
                except Exception as e:
                    break
            print(len(self.emp_list))
        except Exception as e:
            print("No records found")


        assert self.emp_id in self.emp_list
