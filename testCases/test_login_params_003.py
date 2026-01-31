import pytest


from PageObjects.Login_page import Login_Page_Class
from Utilities.readconfig import ReadProperties


class Test_login_params_005:
    driver=None
    login_url=ReadProperties.get_login_url()

    @pytest.mark.usefixtures("browser_setup")
    def test_credkart_login_params_ddt_005(self,browser_setup,credkart_login_data):
       email_id = credkart_login_data[0]
       password_data = credkart_login_data[1]
       expected_result = credkart_login_data[2]

       print(f"email_id-->{email_id}")
       print(f"password-->{password_data}")
       print(f"expected_result-->{expected_result}")

       self.driver.get(self.login_url)

       self.para=Login_Page_Class(self.driver)
       self.para.Enter_Email(email_id)
       self.para.Enter_Password(password_data)
       self.para.Click_Login_Register_Button()
       if self.para.verify_menu_button_visibility()=="pass":
           print("User login pass")
           self.para.Click_Menu_button()
           self.para.Click_Logout_button()

           actual_result = 'login_pass'
       else:
           print("User login fail")
           actual_result = 'login_fail'

       if actual_result==expected_result:
           print("Test case Pass")
       else:
           print("Test case Fail")
           assert False


