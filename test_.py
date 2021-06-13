import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from main import app

client = TestClient(app)


def test_success_calc():
    response = client.post('/calc', json={'number1': 1, 'number2': 2})
    assert response.status_code == 200
    assert response.json() == {'result': 3}


@pytest.mark.parametrize('number1', [0, -1, 'a', 0.2, None])
def test_bad_number1(number1):
    response = client.post('/calc', json={'number1': number1, 'number2': 2})
    assert response.status_code == 422


@pytest.mark.parametrize('number2', [-1, 'a', 0.2, None])
def test_bad_number2(number2):
    response = client.post('/calc', json={'number1': 1, 'number2': number2})
    assert response.status_code == 422


def test_missing_field():
    response = client.post('/calc', json={'number2': 1})
    assert response.status_code == 422


def test_bad_response(mocker):
    with mocker.patch('main.my_sum', return_value=-1):
        with pytest.raises(ValidationError):
            client.post('/calc', json={'number1': 1, 'number2': 2})
