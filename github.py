import requests

class GitHub:
    BASE_URL = "https://api.github.com"

    def get_user(self, username):
        url = f"{self.BASE_URL}/users/{username}"
        response = requests.get(url)
        return response.json()

    def search_repo(self, name):
        url = f"{self.BASE_URL}/search/repositories"
        params = {"q": name}
        response = requests.get(url, params=params)
        return response.json()
