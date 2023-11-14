from src.hrm.driver_base import DriverBase

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


simpeg = "https://simpeg2.jogjaprov.go.id/prod/"


class DriverSimpeg(DriverBase):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def login(self):
        driver = self.driver
        driver.get(simpeg)

        form_username = driver.find_element(By.NAME, 'username')
        form_password = driver.find_element(By.NAME, 'password')

        form_username.send_keys(self.username)
        form_password.send_keys(self.password)
        form_password.send_keys(Keys.RETURN)
