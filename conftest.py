from src.generator.userdata import UserData
import pytest


@pytest.fixture()
def create_user():
    user = UserData().create_user
    return user

@pytest.fixture
def correct_user():
    return {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }