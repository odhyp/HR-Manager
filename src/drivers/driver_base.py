from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class DriverBase:
    def __init__(self):
        """Initialize the DriverBase with a Chrome webdriver.
        """
        self.driver = webdriver.Chrome()

    def quit(self):
        """Quit the webdriver.
        """
        self.driver.quit()

    def wait(self):
        """Create and return a WebDriverWait object with a timeout
        of 10 seconds.
        """
        return WebDriverWait(self.driver, 10)
