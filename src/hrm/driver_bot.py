from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class DriverBot():
    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print(f"Locator type {locatorType} is not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print(f"Element found with locator: {locator} and locatorType: {locatorType}")
        except:
            print(f"Element not found with locator: {locator} and locatorType: {locatorType}")
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print(f"Clicked on element with locator: {locator} and locatorType: {locatorType}")
        except:
            print(f"Cannot click on the element with locator: {locator} and locatorType: {locatorType}")

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print(f"Sent data: {data} on element with locator: {locator} and locatorType: {locatorType}")
        except:
            print(f"Cannot send data on the element with locator: {locator} and locatorType: {locatorType}")

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print(f"Waiting for maximum of {str(timeout)} seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            print(f"Element appeared on the web page")
        except:
            print(f"Element not appeared on the web page")
        return element
