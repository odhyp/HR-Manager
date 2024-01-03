from selenium.common.exceptions import (NoSuchElementException,
                                        ElementClickInterceptedException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from src.drivers.driver_base import DriverBase

presensi = "https://presensi2.jogjaprov.go.id/"
rekap_presensi = "https://presensi2.jogjaprov.go.id/lap-pres/rekap/?menu_id=15"
rekap_prestasi = "https://presensi2.jogjaprov.go.id/lap-pres/prestasi/?menu_id=16"


class DriverPresensi(DriverBase):
    def __init__(self, username: str, password: str):
        """Initialize DriverPresensi with the provided username and password.

        Args:
            username (str): The username for login.
            password (str): The password for login.
        """
        super().__init__()
        self.username = username
        self.password = password

    def login(self):
        """Perform login operation on the Presensi website.
        """
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

    def rekap_presensi(self, tanggal_mulai: str, tanggal_selesai: str, jenis_laporan: str = "detail"):
        """Download 'Rekap Presensi.xls' from the Presensi website.

        Args:
        - tanggal_mulai (str): The start date for the report.
        - tanggal_selesai (str): The end date for the report.
        - jenis_laporan (str, optional): The type of report, either "standard" 
          or "detail". Defaults to "detail".
        """
        driver = self.driver
        driver.get(rekap_presensi)

        try:
            self.wait().until(EC.presence_of_element_located((By.NAME, 'tanggal_mulai')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_nipnama = driver.find_element(By.NAME, 'nipnama')
        form_tanggal_mulai = driver.find_element(By.NAME, 'tanggal_mulai')
        form_tanggal_selesai = driver.find_element(By.NAME, 'tanggal_selesai')
        dropdown_jenis_laporan = driver.find_element(By.NAME, 'jenis_lap_kode')
        dropdown_export_mode = driver.find_element(By.ID, 'fatih')
        button_submit = driver.find_element(By.XPATH, '//*[@id="ahsan"]/div[3]/button')

        form_tanggal_mulai.send_keys(tanggal_mulai)
        form_tanggal_selesai.send_keys(tanggal_selesai)
        Select(dropdown_jenis_laporan).select_by_value(jenis_laporan)
        Select(dropdown_export_mode).select_by_value("excel")

        try:
            button_submit.click()
        except (ElementClickInterceptedException, Exception):
            form_nipnama.send_keys(Keys.RETURN)

    def rekap_prestasi(self, bulan: str):
        """Download 'Rekap Prestasi.xls' from the Presensi website.

        Args:
        - bulan (str): The month for the report.
        """
        driver = self.driver
        driver.get(rekap_prestasi)

        try:
            self.wait().until(EC.presence_of_element_located((By.NAME, 'bulan')))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        form_nipnama = driver.find_element(By.NAME, 'nipnama')
        form_bulan = driver.find_element(By.NAME, 'bulan')
        dropdown_export_mode = driver.find_element(By.ID, 'fatih')
        button_submit = driver.find_element(By.XPATH, '//*[@id="ahsan"]/div[3]/button')

        form_bulan.send_keys(bulan)
        Select(dropdown_export_mode).select_by_value("excel")

        try:
            button_submit.click()
        except (ElementClickInterceptedException, Exception):
            form_nipnama.send_keys(Keys.RETURN)
