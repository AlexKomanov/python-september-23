import requests
from assertpy import assert_that


def test_get_existing_user():
    get_response: requests.Response = requests.get(url='https://reqres.in/api/users/2')
    assert get_response.status_code == 200
    assert_that(get_response.status_code).is_equal_to(200)
    assert get_response.ok == True
    assert_that(get_response.ok).is_true()
    response_json = get_response.json()
    assert 'id' and 'first_name' and 'last_name' in response_json['data'].keys()


def test_get_non_existing_user():
    get_response: requests.Response = requests.get(url='https://reqres.in/api/users/32')
    assert get_response.status_code == 404
    assert_that(get_response.status_code).is_equal_to(404)
    assert get_response.ok == False
    assert_that(get_response.ok).is_false()
    assert_that(get_response.text).is_equal_to('{}')
    assert_that(get_response.reason).is_equal_to('Not Found')


