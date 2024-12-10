import pytest
import requests

@pytest.mark.http
def test_first_request():
    response = requests.get("https://api.github.com/zen")
    print(f"Response text: {response.text}")

    assert response.status_code == 200, "Status code is not 200"

@pytest.mark.http
def test_second_request():
    response = requests.get("https://api.github.com/users/defunkt")
    json_data = response.json()

    assert json_data["name"] == "Chris Wanstrath", "Name does not match 'Chris Wanstrath'"

@pytest.mark.http
def test_status_code_request():
    response = requests.get("https://api.github.com/users/sergii_butenko")
    
    assert response.status_code == 404, "Status code is not 404"