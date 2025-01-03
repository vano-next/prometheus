import pytest

@pytest.mark.api
def test_user_exists(github_api):
    """Перевірка, що користувач існує."""
    response = github_api.get_user("defunkt")
    assert response["login"] == "defunkt", f"Expected login to be 'defunkt', got {response['login']}"

@pytest.mark.api
def test_user_not_exists(github_api):
    """Перевірка, що користувач не існує."""
    response = github_api.get_user("butenkosergii")
    assert response["message"] == "Not Found", f"Expected message to be 'Not Found', got {response['message']}"

@pytest.mark.api
def test_repo_can_be_found(github_api):
    """Перевірка, що репозиторій може бути знайдено."""
    response = github_api.search_repo("become-qa-auto")
    assert response["total_count"] > 0, f"Expected total_count to be greater than 0, got {response['total_count']}"
    assert any(repo["name"] == "become-qa-auto" for repo in response["items"]), "Repository 'become-qa-auto' not found"

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    """Перевірка, що репозиторій не може бути знайдено."""
    response = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert response["total_count"] == 0, f"Expected total_count to be 0, got {response['total_count']}"

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    """Перевірка, що репозиторій із одним символом в імені можна знайти."""
    response = github_api.search_repo("s")
    assert response["total_count"] != 0, "Expected total_count to be non-zero, got 0"
