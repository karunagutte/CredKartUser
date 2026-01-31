
"""
1. Login
2. Registration
3. Checkout
4. Amount Verification
5. Login with params
6.Login with Excel
7. Registration with params
8. Registration with Excel
"""
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Login_page import Login_Page_Class
from PageObjects.Registration_page import Registration_Page_Class
from Utilities.XLUtils import Excel_methods
from Utilities.logger import log_generator_class
from Utilities.readconfig import ReadProperties


@pytest.mark.usefixtures("browser_setup")
class Test_User_Profile:
    driver = None
    email=ReadProperties.get_data_for_email()
    password=ReadProperties.get_data_for_password()
    login_url=ReadProperties.get_login_url()
    registration_url=ReadProperties.get_registration_url()
    log=log_generator_class.gen_log_method()
    #**********Excel Details*****************
    Excel_file=".\\Test_Data\\Credkart_Test_Data.xlsx"
    sheet_name="login_data"


    @pytest.mark.usefixtures("browser_setup")
    def test_Credkart_login_ddt_004(self):

        self.driver.get(self.login_url)
        self.lp = Login_Page_Class(self.driver)  # login page class object and now we can access the methods
        self.log.info("Reading Data from Excel")
        #Total rows in excel
        self.rows=Excel_methods.get_count_rows(self.Excel_file,self.sheet_name)
        self.log.info(f"Number of rows in Excel file {self.rows}")

        result_list=[]
        for i in range (2,self.rows+1):
            self.driver.get(self.login_url)
            self.log.info("Opening Browser and Entering email")
            self.email=Excel_methods.read_excel_data(self.Excel_file,self.sheet_name,i,2)
            self.password=Excel_methods.read_excel_data(self.Excel_file,self.sheet_name,i,3)
            self.expected_result=Excel_methods.read_excel_data(self.Excel_file,self.sheet_name,i,4)

            # Entering Excel data one by one
            self.lp.Enter_Email(self.email)
            self.log.info("Entering password")
            self.lp.Enter_Password(self.password)
            self.log.info("clicking on Login_Register_Button ")
            self.lp.Click_Login_Register_Button()

            if self.lp.verify_menu_button_visibility() == "pass":
                self.log.info("verify_menu_button_visibility pass")
                self.log.info("taking screenshot of pass testcase")
                self.driver.save_screenshot(f".\\Screenshots\\User Login Successful_{self.email}.png")
                self.log.info("clicking on menu button")
                self.lp.Click_Menu_button()
                self.log.info("clicking on logout button")
                self.lp.Click_Logout_button()
                actual_result="login_pass"
                Excel_methods.write_excel_data(self.Excel_file,self.sheet_name,i,5,actual_result)
            else:

                self.log.info("taking screenshot of fail testcase")
                self.driver.save_screenshot(f".\\Screenshots\\User Login Fail {self.email}.png")
                actual_result = "login_fail"
                Excel_methods.write_excel_data(self.Excel_file, self.sheet_name, i, 5, actual_result)

            if actual_result==self.expected_result:
                test_status="Pass"
                Excel_methods.write_excel_data(self.Excel_file,self.sheet_name,i,6,test_status)
            else:
                test_status="Fail"
                Excel_methods.write_excel_data(self.Excel_file,self.sheet_name,i,6,test_status)

            result_list.append(test_status)

        if 'Fail' not in result_list:
            self.log.info("All Testcase Passes")
        else:
            self.log.info("Some of the testcases have failed")
            assert False

        self.log.info("test_Credkart_login_ddt_004 Completed")



