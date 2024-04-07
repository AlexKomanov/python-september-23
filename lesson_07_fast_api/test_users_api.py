import requests
from assertpy import assert_that


def test_get_all_users():
    get_response: requests.Response = requests.get(url='http://127.0.0.1:8000/api/v1/users')
    assert get_response.status_code == 200
    assert_that(get_response.status_code).is_equal_to(200)
    assert get_response.ok == True
    assert_that(get_response.ok).is_true()
    response_json = get_response.json()
    for single_user in response_json:
        assert 'id' in single_user.keys()


def test_get_single_user():
    get_response: requests.Response = requests.get(
        url='http://127.0.0.1:8000/api/v1/users/e3d9650d-5907-4daf-8760-f5343f121b7f')
    assert get_response.status_code == 200
    assert_that(get_response.status_code).is_equal_to(200)
    assert get_response.ok == True
    assert_that(get_response.ok).is_true()
    response_json = get_response.json()
    assert 'id' in response_json


def test_get_single__incorrect_user():
    incorrect_guid = 'e3d9650d-5907-4daf-8760-f5343f121b72'
    get_response: requests.Response = requests.get(
        url=f"http://127.0.0.1:8000/api/v1/users/{incorrect_guid}")
    assert get_response.status_code == 404
    assert_that(get_response.status_code).is_equal_to(404)
    response_json = get_response.json()
    assert response_json['detail'] == f"No user with id '{incorrect_guid}' was found..."
