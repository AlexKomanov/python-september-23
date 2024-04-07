import requests
from assertpy import assert_that
import json


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


def test_delete_single_user():
    all_users_response: requests.Response = requests.get(url='http://127.0.0.1:8000/api/v1/users')
    all_users = all_users_response.json()
    guid = all_users[-1]['id']
    get_response: requests.Response = requests.delete(
        url=f"http://127.0.0.1:8000/api/v1/users/{guid}")
    assert get_response.status_code == 200
    assert_that(get_response.status_code).is_equal_to(200)
    assert get_response.json()['message'] == f"The user with id '{guid}' was removed..."


def test_delete_single__incorrect_user():
    incorrect_guid = 'e3d9650d-5907-4daf-8760-f5343f121b72'
    get_response: requests.Response = requests.delete(
        url=f"http://127.0.0.1:8000/api/v1/users/{incorrect_guid}")
    assert get_response.status_code == 404
    assert_that(get_response.status_code).is_equal_to(404)
    response_json = get_response.json()
    assert response_json['detail'] == f"No user with id '{incorrect_guid}' was found..."


def test_register_new_user():
    headers = {
        'Content-Type': 'application/json',
        "Accept": 'application/json'
    }

    new_user_data = {
        "first_name": "New First Name",
        "last_name": "New Last Name",
        "middle_name": "New Middle Name",
        "gender": "male",
        "roles": [
            "user",
            "admin"
        ]
    }

    post_response = requests.post('http://127.0.0.1:8000/api/v1/users',
                                  json.dumps(new_user_data),
                                  headers=headers)
    assert_that(post_response.status_code).is_equal_to(201)
    # assert_that(post_response.reason).is_equal_to('Bad Request')
    # assert_that(post_response.json()['error']).is_equal_to('Missing password')


def test_register_new_user_2():
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    new_user_data = {
        "first_name": "New First Name",
        "last_name": "New Last Name",
        "middle_name": "New Middle Name",
        "gender": "male",
        "roles": ["user", "admin"],
    }

    post_response = requests.post(
        "http://127.0.0.1:8000/api/v1/users", json.dumps(new_user_data), headers=headers
    )
    assert_that(post_response.status_code).is_equal_to(201)
    # assert_that(post_response.reason).is_equal_to('Bad Request')
    # assert_that(post_response.json()['error']).is_equal_to('Missing password')
