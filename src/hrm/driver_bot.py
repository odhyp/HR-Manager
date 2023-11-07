from selenium import webdriver


class DriverBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def quit(self):
        self.bot.quit()
