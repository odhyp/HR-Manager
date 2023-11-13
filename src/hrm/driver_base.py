from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class DriverBase:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def quit(self):
        self.driver.quit()

    def wait(self):
        return WebDriverWait(self.driver, 10)
