import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


@pytest.mark.ui
def test_google_search_and_navigation():
    # Ініціалізуємо драйвер для Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Переходимо на сайт Google
        driver.get("https://www.google.com/")

        # 2. Вводимо в поле пошуку "35 ОБМП"
        search_field = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_field.send_keys("35 ОБМП")
        search_field.send_keys(Keys.RETURN)

        # 3. У виданому пошуку натискаємо на посилання з назвою
        # "35-та окрема бригада морської піхоти (Україна)"
        target_link = wait.until(EC.presence_of_element_located(
            (By.PARTIAL_LINK_TEXT, "35-та окрема бригада морської піхоти (Україна)")
        ))
        target_link.click()

        # 4. На сайті переходимо за посиланням з текстом
        # "Контрнаступ ЗСУ на півдні України (2023)"
        counteroffensive_link = wait.until(EC.presence_of_element_located(
            (By.LINK_TEXT, "Контрнаступ ЗСУ на півдні України (2023)")
        ))
        counteroffensive_link.click()

        # 5. Перевіряємо, чи є текст "Український контрнаступ 2023 року"
        assert wait.until(EC.text_to_be_present_in_element(
            (By.TAG_NAME, "body"), "Український контрнаступ 2023 року"
        )), "Очікуваний текст не знайдено на сторінці!"

    finally:
        # 6. Закриваємо браузер
        driver.quit()
