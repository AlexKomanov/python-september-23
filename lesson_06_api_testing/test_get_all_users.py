import requests
from assertpy import assert_that


def test_get_all_users_and_validate_id_keys():
    get_response: requests.Response = requests.get(url='https://reqres.in/api/users')
    assert get_response.status_code == 200
    assert_that(get_response.status_code).is_equal_to(200)
    assert get_response.ok == True
    assert_that(get_response.ok).is_true()
    response_json = get_response.json()
    for single_object in response_json['data']:
        assert 'id' in single_object.keys()

