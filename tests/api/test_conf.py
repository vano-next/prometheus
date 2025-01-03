import pytest

class User:
    def __init__(self, name=None, second_name=None):
        self.name = name
        self.second_name = second_name

    def create(self):
        self.name = "Ivan"
        self.second_name = "Lavryk"

    def remove(self):
        self.name = ""
        self.second_name = ""

@pytest.fixture
def user():
    
    user_obj = User()
    user_obj.create()
    yield user_obj
    
    user_obj.remove()