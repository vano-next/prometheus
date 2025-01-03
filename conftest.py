import pytest
from modules.api.clients.github import GitHub

@pytest.fixture
def github_api():
    """Фікстура для роботи з GitHub API."""
    return GitHub()
