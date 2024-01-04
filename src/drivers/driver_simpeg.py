import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.constants import (NAMA_UNOR,
                           URL_SIMPEG,
                           URL_SIMPEG_NOMINATIF,
                           URL_SIMPEG_DUK,
                           WAIT_TIME)
from src.drivers.driver_base import DriverBase


class DriverSimpeg(DriverBase):
    def __init__(self, username: str, password: str):
        """Initialize DriverSimpeg with the provided username and password.

        Args:
        - username (str): The username for login.
        - password (str): The password for login.
        """
        super().__init__()
        self.username = username
        self.password = password

    def login(self):
        """Perform login operation on the Simpeg website.
        """
        driver = self.driver
        driver.get(URL_SIMPEG)

        try:
            self.wait().until(EC.presence_of_element_located(
                (By.NAME, "username")))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_username = driver.find_element(By.NAME, 'username')
        form_password = driver.find_element(By.NAME, 'password')

        form_username.send_keys(self.username)
        form_password.send_keys(self.password)
        form_password.send_keys(Keys.RETURN)

        try:
            self.wait().until(EC.presence_of_element_located(
                (By.CLASS_NAME, 'sidebar-menu')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

    def nominatif(self):
        """Download 'Nominatif.xls' from the Simpeg website.
        """
        driver = self.driver
        driver.get(URL_SIMPEG_NOMINATIF)

        try:
            self.wait().until(EC.presence_of_element_located((By.ID, 'tb')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_nama_unor = driver.find_element(
            By.XPATH, '//*[@id="tb"]/span[2]/input[1]')
        button_export = driver.find_element(By.CLASS_NAME, 'btn-primary')

        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(NAMA_UNOR)
        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(Keys.ARROW_DOWN)
        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(Keys.RETURN)
        time.sleep(WAIT_TIME)
        button_export.click()

    def duk(self):
        """Download 'Daftar_Urut_Kepangkatan.xls' from the Simpeg website.
        """
        driver = self.driver
        driver.get(URL_SIMPEG_DUK)

        try:
            self.wait().until(EC.presence_of_element_located((By.ID, 'tb')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_nama_unor = driver.find_element(
            By.XPATH, '//*[@id="tb"]/span[2]/input[1]')
        button_export = driver.find_element(By.CLASS_NAME, 'btn-primary')

        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(NAMA_UNOR)
        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(Keys.ARROW_DOWN)
        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(Keys.RETURN)
        time.sleep(WAIT_TIME)
        button_export.click()
