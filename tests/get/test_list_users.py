import pytest
import requests
from base.response import Response
from src.schemas.user import Resp
from base.end_points import end_point


@pytest.mark.parametrize("status, page", [(200, '2'), (200, '4')])
def test_status_code_get_list_users(status, page):
    response = requests.get(end_point['list_users']+page)
    Response(response).assert_status_code(status)

@pytest.mark.parametrize("model, page", [(Resp, '1'), (Resp, '20')])
def test_validate_response(model, page):
    response = requests.get(end_point['list_users']+page)
    Response(response).validate_response(model)

@pytest.mark.parametrize("count, page", [(6, '1')])
def test_validate_users_count(count, page):
    response = requests.get(end_point['list_users']+page)
    assert len(response.json()['data']) == count, 'Ошибка в количестве пользователей'