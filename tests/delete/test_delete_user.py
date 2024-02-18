import pytest
import requests
from base.response import Response
from base.end_points import end_point

@pytest.mark.parametrize("user", ['2'])
def test_delete_user(user):
    response = requests.delete(end_point['single_user'] + user)
    assert response.status_code == 204, 'Ошибка в коде ответа'

