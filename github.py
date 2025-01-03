import requests

class GitHub:
    BASE_URL = "https://api.github.com"

    def get_user(self, username):
        """Отримати інформацію про користувача."""
        url = f"{self.BASE_URL}/users/{username}"
        response = requests.get(url)
        return response.json()

    def search_repo(self, name):
        """Пошук репозиторіїв."""
        url = f"{self.BASE_URL}/search/repositories"
        params = {"q": name}
        response = requests.get(url, params=params)
        return response.json()

    def get_emojis(self):
        """Отримати список Emoji."""
        url = f"{self.BASE_URL}/emojis"
        response = requests.get(url)
        return response.json()

    def list_commits(self, owner, repo):
        """Отримати список комітів для репозиторію."""
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/commits"
        response = requests.get(url)
        return response.json()
    