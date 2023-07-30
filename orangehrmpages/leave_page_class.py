import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from utilities.util import scroll_to_page, wait_for_element


class HrmLeavePg:
    leave_link = '//span[text()="Leave"]'
    leave_heading = '//h5[text()="Leave List"]'
    leave_from_date_label = '//label[text()="From Date"]'
    leave_to_Date_label = '//label[text()="To Date"]'
    footer_text_for_scroll = "//a[text()='OrangeHRM, Inc']"
    date_filter_results = "//div[text()='Date']"

    def __init__(self, a_driver):
        self.my_driver = a_driver
        self.my_driver.implicitly_wait(5)

    def navigate_to_leave_page(self):
        self.my_driver.find_element(By.XPATH, self.leave_link).click()
        self.verify_leave_page_heading()

    def verify_leave_page_heading(self):
        header_text = self.my_driver.find_element(By.XPATH, self.leave_heading)
        if header_text is not None:
            return True

    def verify_dates(self):
        leave_from_date_label_element = self.my_driver.find_element(By.XPATH, self.leave_from_date_label)
        leave_from_date = self.my_driver.find_element(locate_with(By.TAG_NAME, "input").below(leave_from_date_label_element))
        leave_from_date.click()
        leave_from_date.send_keys(str(datetime.date.today()))
        wait_for_element(self.my_driver, self.date_filter_results)

    def scroll_to_results(self):
        footer_text_element = self.my_driver.find_element(By.XPATH, self.footer_text_for_scroll)
        scroll_to_page(self.my_driver, footer_text_element)
