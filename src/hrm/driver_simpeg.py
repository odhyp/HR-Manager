from driver_base import DriverBase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from utils import get_username, get_password

simpeg = "https://simpeg2.jogjaprov.go.id/prod/"


class DriverSimpeg(DriverBase):
    def __init__(self):
        super().__init__()
        driver = self.driver
        driver.get(simpeg)

    def login(self):
        driver = self.driver

        username = get_username()
        password = get_password()

        form_username = driver.find_element(By.NAME, 'username')
        form_password = driver.find_element(By.NAME, 'password')

        form_username.send_keys(username)
        form_password.send_keys(password)
        form_password.send_keys(Keys.RETURN)

        time.sleep(5)

        driver.quit()
