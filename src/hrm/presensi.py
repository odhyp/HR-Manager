from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


with WebDriver(webdriver.Chrome()) as wd:
    wd.maximize_window()
    wd.get('https://presensi2.jogjaprov.go.id/')

    username = wd.find_element(By.NAME, "username")
    password = wd.find_element(By.NAME, "password")
    username.send_keys("197708151998032002")
    password.send_keys("Feri2022#")
    password.send_keys(Keys.RETURN)
    wd.get("https://presensi2.jogjaprov.go.id/lap-pres/rekap/?menu_id=15")
    tanggal_mulai = wd.find_element(By.NAME, "tanggal_mulai")
    tanggal_selesai = wd.find_element(By.NAME, "tanggal_selesai")
    tanggal_mulai.send_keys("2023-10-01")
    tanggal_selesai.send_keys("2023-10-31")
    find_export_mode = wd.find_element(By.ID, 'fatih')
    select_export_mode = Select(find_export_mode)
    select_export_mode.select_by_value("excel")

    submit = wd.find_element(By.XPATH, '//*[@id="ahsan"]/div[3]/button')
    submit.click()

    time.sleep(10)
