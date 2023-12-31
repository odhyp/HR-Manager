from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time

from src.drivers.driver_base import DriverBase

WAIT_TIME = 3.5

simpeg = "https://simpeg2.jogjaprov.go.id/prod/"
nominatif = "https://simpeg2.jogjaprov.go.id/prod/index.php/listing/nominatif"
duk = "https://simpeg2.jogjaprov.go.id/prod/index.php/duk"
nama_unor = "Kantor Pelayanan Pajak Daerah Daerah Istimewa Yogyakarta di Kabupaten Bantul"


class DriverSimpeg(DriverBase):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def login(self):
        driver = self.driver
        driver.get(simpeg)

        try:
            self.wait().until(EC.presence_of_element_located((By.NAME, "username")))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_username = driver.find_element(By.NAME, 'username')
        form_password = driver.find_element(By.NAME, 'password')

        form_username.send_keys(self.username)
        form_password.send_keys(self.password)
        form_password.send_keys(Keys.RETURN)

        try:
            self.wait().until(EC.presence_of_element_located((By.CLASS_NAME, 'sidebar-menu')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

    def nominatif(self):
        driver = self.driver
        driver.get(nominatif)

        try:
            self.wait().until(EC.presence_of_element_located((By.ID, 'tb')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_nama_unor = driver.find_element(By.XPATH, '//*[@id="tb"]/span[2]/input[1]')
        button_export = driver.find_element(By.CLASS_NAME, 'btn-primary')

        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(nama_unor)
        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(Keys.ARROW_DOWN)
        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(Keys.RETURN)
        time.sleep(WAIT_TIME)
        button_export.click()

    def duk(self):
        driver = self.driver
        driver.get(duk)

        try:
            self.wait().until(EC.presence_of_element_located((By.ID, 'tb')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_nama_unor = driver.find_element(By.XPATH, '//*[@id="tb"]/span[2]/input[1]')
        button_export = driver.find_element(By.CLASS_NAME, 'btn-primary')

        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(nama_unor)
        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(Keys.ARROW_DOWN)
        time.sleep(WAIT_TIME)
        form_nama_unor.send_keys(Keys.RETURN)
        time.sleep(WAIT_TIME)
        button_export.click()
