from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By


class DriverWrapper:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(
        self,
        locator,
        timeout=10,
        pollFrequency=0.5,
        invisible=False,
        condition=EC.visibility_of_element_located,
    ):
        wait = WebDriverWait(
            self.driver,
            timeout,
            poll_frequency=pollFrequency,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException,
            ],
        )
        if invisible:
            element = wait.until_not(
                condition((locator["by"], locator["locator"])))
        else:
            element = wait.until(
                condition((locator["by"], locator["locator"])))
        return element

    def click_element(self, locator):
        self.wait_for_element(locator, condition=EC.element_to_be_clickable)
        element = self.get_element(locator)
        element.click()
        return element

    def send_keys(self, data, locator):
        element = self.get_element(locator)
        element.send_keys(data)
        return element

    def get_element(self, locator):
        element = self.driver.find_element(locator["by"], locator["locator"])
        return element
