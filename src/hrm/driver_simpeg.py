from src.hrm.driver_base import DriverBase

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

simpeg = "https://simpeg2.jogjaprov.go.id/prod/"


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
