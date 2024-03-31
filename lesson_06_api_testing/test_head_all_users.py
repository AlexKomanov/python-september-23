import requests
from assertpy import assert_that


def test_head_all_users():
    head_response: requests.Response = requests.head(url='https://reqres.in/api/users')
    assert head_response.status_code == 200
    assert_that(head_response.status_code).is_equal_to(200)
    assert head_response.ok == True
    assert_that(head_response.ok).is_true()
