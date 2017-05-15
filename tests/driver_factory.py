import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    if os.environ.get('SAUCE', None):
        sauce_user = os.environ.get('SAUCE_USER')
        sauce_key = os.environ.get('SAUCE_KEY')
        desired_cap = {
            'platform': "Mac OS X 10.12",
            'browserName': "chrome",
            'version': "58",
        }
        return webdriver.Remote(
            command_executor='http://{}:{}@ondemand.saucelabs.com:80/wd/hub'.format(sauce_user, sauce_key),
            desired_capabilities=desired_cap)

    flavor = os.environ.get('DRIVER', 'chrome')

    if flavor == 'firefox':
        return webdriver.Firefox()
    elif flavor == 'edge':
        return webdriver.Edge()
    elif flavor == 'safari':
        return webdriver.Safari()
    elif flavor == 'phantomjs':
        return webdriver.PhantomJS()
    else:
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {
            'credentials_enable_service': False,
            'profile': {
                'password_manager_enabled': False
            }
        })

        return webdriver.Chrome(chrome_options=chrome_options)
