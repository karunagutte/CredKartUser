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

    def test_verify_Credkart_url_001(self):
        # driver=webdriver.Chrome()
        # driver.maximize_window()

        #self.driver.get("https://automation.credence.inp/")
        self.log.info("Opening Browser")
        self.driver.get(self.login_url)
        if self.driver.title=="CredKart":
            self.log.info("test_verify_Credkart_url_001 is passed")
            print(f"Title of Page : {self.driver.title}")
            self.log.info("Taking Screenshot of pass testcase")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_pass.png")
        else:
            self.log.info("Taking Screenshot of pass testcase")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_fail.png")
            assert False

    @pytest.mark.usefixtures("browser_setup")
    def test_Credkart_login_002(self):
        #self.driver.get("https://automation.credence.in/login")
        self.driver.get(self.login_url)
        # email_id = "Credencetest@test.com"
        # pass_word = "Credence@123"

        self.lp = Login_Page_Class(self.driver)  # login page class object and now we can access the methods

        # Enter Username
        # email = self.driver.find_element(By.XPATH, "//input[@id='email']")
        # email.send_keys(email_id)
        self.log.info("Entering email")
        self.lp.Enter_Email(self.email)

        # Enter Password
        # password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        # password.send_keys(pass_word)
        self.log.info("Entering password")
        self.lp.Enter_Password(self.password)

        # Click on Login button
        # login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # login_button.click()
        self.log.info("clicking on Login_Register_Button ")
        self.lp.Click_Login_Register_Button()

        # wait = WebDriverWait(self.driver, 5)
        # try:
        #     wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
        #     element = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        #     print("User Login Successful")
        #     # driver.save_screenshot(f"User Login Successful_{email_id}.png")
        #     menu = self.driver.find_element(By.XPATH, "//a[@role='button']")
        #     menu.click()
        #     logout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        #     logout.click()
        #
        #
        # except:
        #     print("User Login Fail")
        #     # driver.save_screenshot(f"User Login Fail_{email_id}.png")
        #     assert False, "User Login Fail"

        if self.lp.verify_menu_button_visibility() == "pass":
            self.log.info("verify_menu_button_visibility pass")
            self.log.info("taking screenshot of pass testcase")
            self.driver.save_screenshot(f".\\Screenshots\\User Login Pass {self.email}.png")
            self.log.info("clicking on menu button")
            self.lp.Click_Menu_button()
            self.log.info("clicking on logout button")
            self.lp.Click_Logout_button()
        else:
            self.log.info("taking screenshot of fail testcase")
            self.driver.save_screenshot(f".\\Screenshots\\User Login Fail {self.email}.png")
            assert False, "User Login Fail"
        # self.driver.quit()

    def test_Credkart_registration_003(self):

        #self.driver.get("https://automation.credence.in/register")
        self.driver.get(self.registration_url)
        fake_username = Faker().user_name()  # New
        fake_email = Faker().email()  # New
        password_data = "Credence_user_101@123"
        self.log.info("printing fake username")
        print(f"fake_username--> {fake_username}")  # New
        self.log.info("printing fake password")
        print(f"fake_email--> {fake_email}")  # New

        self.rp = Registration_Page_Class(self.driver)
        # Enter Username
        self.log.info("entering username")
        self.rp.Enter_Name(fake_username)
        # Enter Email
        self.log.info("entering email")
        self.rp.Enter_Email(fake_email)
        # Enter Password
        self.log.info("entering password")
        self.rp.Enter_Password(password_data)
        # Enter Confirm Password
        self.log.info("entering confirmed password")
        self.rp.Enter_Confirm_Password(password_data)
        # Click on register button
        self.log.info("clicking on register button")
        self.rp.Click_Login_Register_Button()

        if self.rp.verify_menu_button_visibility() == "pass":
            self.log.info("Menu button visibility passed")
            self.log.info(f"Taking screenshot of User Registration Pass {fake_username}")
            self.driver.save_screenshot(f"User Registration Successful_{fake_username}.png")
            self.log.info("clicking on menu button")
            self.rp.Click_Menu_button()
            self.log.info("clicking on logout button")
            self.rp.Click_Logout_button()
        else:
            self.log.info(f"Taking screenshot of User Registration Fail {fake_username}")
            self.driver.save_screenshot(f"User Registration Fail_{fake_username}.png")
            assert False, "User Registration Fail"

