import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager


@pytest.mark.ui
def test_rozetka_search():
    # Ініціалізація драйвера Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        # Відкриваємо сайт Rozetka
        driver.get("https://rozetka.com.ua/")

        # Знаходимо поле для пошуку
        search_field = driver.find_element(By.CSS_SELECTOR, "input[rzsearchinput='']")
        search_field.send_keys("собака на сіні")

        # Натискаємо клавішу Enter для виконання пошуку
        search_field.send_keys(Keys.RETURN)

        # Чекаємо на результати пошуку
        try:
            results = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".goods-tile__title"))
            )
            assert len(results) > 0, "Результати пошуку не знайдені!"
        except TimeoutException:
            pytest.fail("Результати пошуку не з'явилися вчасно!")
    finally:
        # Закриваємо браузер
        driver.quit()
