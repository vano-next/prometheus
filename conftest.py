import pytest
from modules.api.clients.github import GitHub
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    # Ініціалізація драйвера Firefox
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver  # Повертає драйвер для використання в тестах
    driver.quit()  # Закриває драйвер після тесту



@pytest.fixture
def github_api():
    """Фікстура для роботи з GitHub API."""
    return GitHub()
