from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*locator))
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements(*locator))
        return self.driver.find_elements(*locator)
