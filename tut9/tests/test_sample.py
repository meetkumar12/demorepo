# test_sample.py
from unittest import mock
from tut9.myapp.sample import guess_number , get_ip
import pytest
import requests

@pytest.mark.parametrize("_input , expected", [(3 ,"you  won"), (4 , "you lost")])
@mock.patch("tut9.myapp.sample.roll_dice")
def test_guess_number(mock_roll_dice , _input , expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()


@mock.patch("tut9.myapp.sample.requests.get")
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value =  mock.Mock(name = "mock response" , **{"status_code" : 200 , "json.return_value":{"origin" : "0.0.0.0"}})

    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("http://httpbin.org/ip")