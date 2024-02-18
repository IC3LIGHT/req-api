import pytest
import requests
from base.response import Response
from src.schemas.user import User
from base.end_points import end_point


@pytest.mark.parametrize("status", [201])
def test_status_code_post_user(create_user, status):
    user_data = create_user()
    response = requests.post(end_point['create_user'], data=user_data)
    Response(response).assert_status_code(status)

@pytest.mark.parametrize("model", [User])
def test_validate_response(model, create_user):
    user_data = create_user()
    response = requests.post(end_point['create_user'], data=user_data)
    Response(response).validate_response(model)


def test_correct_data(create_user):
    user_data = create_user()
    response = requests.post(end_point['create_user'], data=user_data)
    Response(response).assert_user_data(user_data)
