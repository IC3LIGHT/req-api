import pytest
import requests
from base.response import Response
from src.schemas.user import UserModel
from base.end_points import end_point


@pytest.mark.parametrize("status, user", [(200, '2'), (404, '333')])
def test_status_code_get_single_user(status, user):
    response = requests.get(end_point['single_user'] + user)
    Response(response).assert_status_code(status)


@pytest.mark.parametrize("model, user", [(UserModel, '1')])
def test_validate_response(model, user):
    response = requests.get(end_point['single_user'] + user)
    Response(response).validate_response(model)


