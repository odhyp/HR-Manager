from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class DriverBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def quit(self):
        self.bot.quit()

    def login_presensi(self):
        bot = self.bot
        bot.maximize_window()
        bot.get('https://presensi2.jogjaprov.go.id/')

        time.sleep(1)

        username = bot.find_element(By.NAME, 'username')
        password = bot.find_element(By.NAME, 'password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

        time.sleep(1)

        print("Login success")
