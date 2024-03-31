import requests
from assertpy import assert_that


def test_delete_user():
    delete_response: requests.Response = requests.delete(url='https://reqres.in/api/users/32')
    assert delete_response.status_code == 204
    assert_that(delete_response.status_code).is_equal_to(204)
    assert delete_response.reason == 'No Content'
    assert_that(delete_response.text).is_equal_to('')
    assert_that(delete_response.reason).is_equal_to('No Content')
