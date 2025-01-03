from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class BasePage:
    def __init__(self):
        # Ініціалізація драйвера Firefox
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def quit(self):
        # Закриття браузера після тесту
        self.driver.quit()
