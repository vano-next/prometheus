import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# GitHub токен
os.environ['GH_TOKEN'] = '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'

@pytest.mark.ui
def test_search_parcel():
    # Ініціалізуємо драйвер для Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        # Відкриваємо сторінку Нової Пошти
        driver.get("https://tracking.novaposhta.ua/")

        # Очікуємо, поки елемент для вводу номера посилки стане доступним
        wait = WebDriverWait(driver, 10)
        tracking_field = wait.until(EC.presence_of_element_located((By.ID, "en")))

        # Вводимо номер накладної
        tracking_field.send_keys("20451075486252")

        # Очікуємо, поки кнопка пошуку стане доступною (не disabled)
        search_button = wait.until(EC.element_to_be_clickable((By.ID, "np-number-input-desktop-btn-search-en")))

        # Натискаємо кнопку пошуку
        search_button.click()

        # Чекаємо, поки URL зміниться на очікувану сторінку
        WebDriverWait(driver, 10).until(EC.url_to_be("https://tracking.novaposhta.ua/#/uk/chat/messages"))

        # Перевіряємо, чи поточний URL співпадає з очікуваним
        assert driver.current_url == "https://tracking.novaposhta.ua/#/uk/chat/messages"

    finally:
        # Закриваємо браузер після тесту
        driver.quit()
