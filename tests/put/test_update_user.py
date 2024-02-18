import pytest
import requests
from base.response import Response
from src.schemas.user import UpdateUser
from base.end_points import end_point


@pytest.mark.parametrize("status, user", [(200, '1'), (200, '333')])
def test_status_code_update_user(create_user, status, user):
    user_data = create_user()
    response = requests.put(end_point['single_user'] + user, data=user_data)
    Response(response).assert_status_code(status)


@pytest.mark.parametrize("model, user", [(UpdateUser, '1'), (UpdateUser, '2')])
def test_validate_response(model, user, create_user):
    user_data = create_user()
    response = requests.put(end_point['single_user'] + user, data=user_data)
    Response(response).validate_response(model)


@pytest.mark.parametrize("user", ['2'])
def test_correct_data(create_user, user):
    user_data = create_user()
    response = requests.put(end_point['single_user'] + user, data=user_data)
    Response(response).assert_user_data(user_data)
