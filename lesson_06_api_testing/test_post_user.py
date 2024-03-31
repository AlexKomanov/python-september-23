import requests
from assertpy import assert_that
import json


def test_register_user_no_success():
    headers = {
        'Content-Type': 'application/json',
        "Accept": 'application/json'
    }

    post_response = requests.post('https://reqres.in/api/register',
                                  json.dumps({"email": "peter@klaven"}),
                                  headers=headers)
    assert_that(post_response.status_code).is_equal_to(400)
    assert_that(post_response.reason).is_equal_to('Bad Request')
    assert_that(post_response.json()['error']).is_equal_to('Missing password')
