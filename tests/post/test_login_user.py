import pytest
import requests
from base.response import Response
from src.schemas.user import Login
from base.end_points import end_point


@pytest.mark.parametrize("status", [200])
def test_status_code_login_user(correct_user, status):
    user_data = correct_user
    response = requests.post(end_point['register'], data=user_data)
    Response(response).assert_status_code(status)

@pytest.mark.parametrize("status", [400])
def test_wrong_code_login_user(create_user, status):
    user_data = create_user()
    response = requests.post(end_point['register'], data=user_data)
    Response(response).assert_status_code(status)



@pytest.mark.parametrize("model", [Login])
def test_model_login_user(model, correct_user):
    user_data = correct_user
    response = requests.post(end_point['register'], data=user_data)
    Response(response).validate_response(model)

