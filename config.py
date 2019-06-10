import sys
import os
from time import sleep
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


# Wait for nodes to be registered
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

ROBOT_BROWSER_TIMEOUT = 30
TIMEOUT     = "20s"
POLLTIME    = "2s"

def check_browser(url):
    elapsed_time = 0
    while elapsed_time != ROBOT_BROWSER_TIMEOUT:
        try:
            driver = webdriver.Remote(
                command_executor=url,
                desired_capabilities=getattr(DesiredCapabilities, 'CHROME')
            )
            driver.quit()
            break
        except:
            sleep(1)
            elapsed_time+=1

TEST_URL             = os.getenv('PROJECT_URL')
BROWSER              = os.getenv('BROWSER')
COMMAND_EXECUTOR     = os.getenv('SELENIUM_HUB')
DESIRED_CAPABILITIES = {'browserName': BROWSER}
if not BROWSER:
    BROWSER = 'chrome'
elif BROWSER == 'ie':
    DESIRED_CAPABILITIES = {'browserName': 'IE', 'browser_version': '11.0', 'os': 'Windows', 'os_version': '8.1', 'resolution': '1024x768', 'browserstack.local': True}
elif BROWSER == 'safari':
    DESIRED_CAPABILITIES = {'browserName': 'Safari', 'browser_version': '10.1', 'os': 'OS X', 'os_version': 'Sierra', 'resolution': '1024x768', 'browserstack.safari.enablePopups': False, 'browserstack.local': True}
elif BROWSER == 'iphone':
    DESIRED_CAPABILITIES = {'browserName': 'iPhone', 'platform': 'MAC', 'device': 'iPhone 6S Plus', 'browserstack.safari.enablePopups': False, 'browserstack.local': True}
elif BROWSER == 'android':
    DESIRED_CAPABILITIES = {'browserName': 'android', 'platform': 'ANDROID', 'device': 'Samsung Galaxy S5', 'browserstack.local': True}


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

test_session = {
    'role': 'business owner',  # Default user is business owner
    'username': None,
    'password': None,
    'login_method': 'PAGE'  # Default login is through login page
}
