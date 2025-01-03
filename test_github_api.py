import pytest

@pytest.mark.api
def test_emojis_exist(github_api):
    """Перевірка, що список Emoji доступний."""
    emojis = github_api.get_emojis()
    assert len(emojis) > 0, "No emojis found"
    sample_emoji_key = list(emojis.keys())[0]  # Беремо перший доступний ключ
    assert sample_emoji_key in emojis, f"Expected emoji '{sample_emoji_key}' not found"

@pytest.mark.api
def test_commits_exist(github_api):
    """Перевірка, що коміти існують для репозиторію."""
    commits = github_api.list_commits("octocat", "Hello-World")
    assert len(commits) > 0, "No commits found for the repository"
    assert "commit" in commits[0], "Expected commit data in response"

@pytest.mark.api
def test_specific_commit_message(github_api):
    """Перевірка, що певний коміт містить повідомлення."""
    commits = github_api.list_commits("octocat", "Hello-World")
    commit_message = commits[0]["commit"]["message"]
    assert len(commit_message) > 0, "Commit message is empty"

@pytest.mark.api
def test_emojis_smile_exists(github_api):
    """Перевірка наявності emoji '+1'."""
    emojis = github_api.get_emojis()
    assert "+1" in emojis, "Emoji '+1' not found"
