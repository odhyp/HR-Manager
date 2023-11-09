from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class DriverBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def quit(self):
        self.bot.quit()

    def wait(self):
        return WebDriverWait(self.bot, 10)

    def login(self):
        bot = self.bot
        bot.maximize_window()
        bot.get('https://presensi2.jogjaprov.go.id/')

        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "form-group")))
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        # Elements
        username = bot.find_element(By.NAME, 'username')
        password = bot.find_element(By.NAME, 'password')

        # Actions
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "mainnav-menu")))
            print("found mainnav-menu")
        except NoSuchElementException:
            print(NoSuchElementException)
            self.quit()

        print("Login success")

    def rekap_presensi(self):
        bot = self.bot
        bot.get("https://presensi2.jogjaprov.go.id/lap-pres/rekap/?menu_id=15")

        # Elements
        tanggal_mulai = bot.find_element(By.NAME, "tanggal_mulai")
        tanggal_selesai = bot.find_element(By.NAME, "tanggal_selesai")
        export_mode = bot.find_element(By.ID, 'fatih')
        submit = bot.find_element(By.XPATH, '//*[@id="ahsan"]/div[3]/button')

        # Actions
        tanggal_mulai.send_keys("2023-11-01")
        tanggal_selesai.send_keys("2023-11-07")
        Select(export_mode).select_by_value("excel")
        submit.click()

        print("File downloaded")

    def rekap_prestasi(self):
        bot = self.bot
        bot.get("https://presensi2.jogjaprov.go.id/lap-pres/prestasi/?menu_id=16")

        # Elements
        bulan = bot.find_element(By.NAME, "bulan")
        export_mode = bot.find_element(By.ID, 'fatih')
        submit = bot.find_element(By.XPATH, '//*[@id="ahsan"]/div[3]/button')

        # Actions
        bulan.send_keys("11/2023")
        Select(export_mode).select_by_value("excel")
        submit.click()

        print("File downloaded")
