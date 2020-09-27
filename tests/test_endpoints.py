import os
import pytest
import requests
from openapi_spec_validator import validate_spec_url

@pytest.mark.parametrize(
    'payload,expected', [
    ({"raw_string": "hello world!"}, "l r!"),
    ({"raw_string": "robinsoncrusoe"}, "bscs"),
    ({"raw_string": ""}, ""),
    ({"raw_string": "ab"}, ""),
    ({"raw_string": "123456"}, "36"),
    ({"raw_string": "!@#$%"}, "#"),
    ({"raw_string": "   "}, " "),
])
def test_string_chopper_expected(host, payload, expected):
    endpoint = os.path.join(host, 'test')
    response = requests.post(endpoint, json=payload)
    assert response.status_code ==200
    json = response.json()
    assert 'chopped_string' in json
    assert json['chopped_string'] == expected

@pytest.mark.parametrize(
    'payload', [
    ({"wrong_param": "hello world!"}),
    ({"string": "hello world!"}),
    ({"": "hello world!"}),
    ({}),
    (),
])
def test_string_chopper_exception(host, payload):
    endpoint = os.path.join(host, 'test')
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 400
    json = response.json()
    assert 'message' in json
    assert json['message'] == 'Request body must be JSON object including key `raw_string` and a string value'

def test_swagger_specification(host):
    endpoint = os.path.join(host, 'api', 'swagger.json')
    validate_spec_url(endpoint)