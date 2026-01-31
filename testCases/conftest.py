import pytest
from selenium import webdriver


#Browser setup code
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser_setup(request):
  browser=request.config.getoption("--browser")
  if browser=="chrome":
      print("Opening Chrome Browser")
      #driver=webdriver.Chrome()
      chrome_options=webdriver.ChromeOptions()
      # Create an "options" object for Chrome.
      # We use it to control Chrome settings before the browser launches, for password message
      chrome_options.add_experimental_option("prefs", {
          "credentials_enable_service": False,
          # This turns OFF Chrome's "credentials service"
          # Chrome will not offer to save usernames/passwords.
          "profile.password_manager_enabled": False
          # This turns OFF Chrome's built-in Password Manager feature.
          # Password Manager related popups (Save password / breach warning) will not come.
         })
      driver=webdriver.Chrome(options=chrome_options)

  elif  browser=="firefox":
      print("Opening Firefox Browser")
      driver=webdriver.Firefox()
  elif browser=="edge":
       print("Opening Edge Browser")
       driver=webdriver.Edge()
  elif browser == "headless":
        print("\nOpening chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options = chrome_options)
  else:
      chrome_options = webdriver.ChromeOptions()
      # Create an "options" object for Chrome.
      # We use it to control Chrome settings before the browser launches, for password message
      chrome_options.add_experimental_option("prefs", {
          "credentials_enable_service": False,
          # This turns OFF Chrome's "credentials service"
          # Chrome will not offer to save usernames/passwords.
          "profile.password_manager_enabled": False
          # This turns OFF Chrome's built-in Password Manager feature.
          # Password Manager related popups (Save password / breach warning) will not come.
      })
      driver = webdriver.Chrome(options=chrome_options)

  driver.maximize_window()
  driver.implicitly_wait(5)

  request.cls.driver=driver
  yield driver
  print("Browser Closed")
  driver.quit()


def pytest_metadata(metadata):
    metadata["Project Name"]="CredKart Automation"
    metadata["Environment"]="QA Environment"
    metadata["Tester Name"]="Credence"

    del metadata["Platform"]

def pytest_html_report_title(report):
    report.title = "Automation Test Execution Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        "Automation Execution Summary",
        "Project: Credence",
        "Executed by: Karuna"
    ]),
    summary.extend([
        "Automation Execution Summary",
        "Project: Credence",
        "Executed by: Karuna"
    ]),
    postfix.extend([
        "Automation Execution Summary",
        "Project: Credence",
        "Executed by: Karuna"
    ])

@pytest.fixture(params=[
        ("Credencetest@test.com", "Credence@123", "login_pass"),  # All correct #
        ("Credencetest@test.com11", "Credence@123", "login_fail"),  # username wrong #
        ("Credencetest@test.com", "Credence@1231", "login_fail"),  # password wrong
        ("Credencetest@test.com1", "Credence@1231", "login_fail")  # username and password wrong
])

def credkart_login_data(request):
    return request.param