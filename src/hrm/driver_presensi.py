from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from src.hrm.driver_base import DriverBase

presensi = "https://presensi2.jogjaprov.go.id/"
rekap_presensi = "https://presensi2.jogjaprov.go.id/lap-pres/rekap/?menu_id=15"
rekap_prestasi = "https://presensi2.jogjaprov.go.id/lap-pres/prestasi/?menu_id=16"


class DriverPresensi(DriverBase):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def login(self):
        driver = self.driver
        driver.get(presensi)

        try:
            self.wait().until(EC.presence_of_element_located((By.NAME, 'username')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_username = driver.find_element(By.NAME, 'username')
        form_password = driver.find_element(By.NAME, 'password')

        form_username.send_keys(self.username)
        form_password.send_keys(self.password)
        form_password.send_keys(Keys.RETURN)

        try:
            self.wait().until(EC.presence_of_element_located((By.ID, 'mainnav-menu')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

    def rekap_presensi(self):
        driver = self.driver
        driver.get(rekap_presensi)

        try:
            self.wait().until(EC.presence_of_element_located((By.NAME, 'tanggal_mulai')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_tanggal_mulai = driver.find_element(By.NAME, 'tanggal_mulai')
        form_tanggal_selesai = driver.find_element(By.NAME, 'tanggal_selesai')
        dropdown_export_mode = driver.find_element(By.ID, 'fatih')
        button_submit = driver.find_element(By.XPATH, '//*[@id="ahsan"]/div[3]/button')

        form_tanggal_mulai.send_keys("2023-11-13")
        form_tanggal_selesai.send_keys("2023-11-14")
        Select(dropdown_export_mode).select_by_value("excel")
        button_submit.click()

    def rekap_prestasi(self):
        driver = self.driver
        driver.get(rekap_prestasi)

        try:
            self.wait().until(EC.presence_of_element_located((By.NAME, 'bulan')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_bulan = driver.find_element(By.NAME, 'bulan')
        dropdown_export_mode = driver.find_element(By.ID, 'fatih')
        button_submit = driver.find_element(By.XPATH, '//*[@id="ahsan"]/div[3]/button')

        form_bulan.send_keys("11/2023")
        Select(dropdown_export_mode).select_by_value("excel")
        button_submit.click()
