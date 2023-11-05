from selenium import webdriver


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


with WebDriver(webdriver.Chrome()) as wd:
    wd.get('https://presensi2.jogjaprov.go.id/')
    print(wd.page_source)
