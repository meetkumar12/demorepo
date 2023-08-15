# test_sample.py

import pytest
from tut2.myapp.sample import validate_age


def test_validate_age_valid_age():
    validate_age(10)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError) as exp_info:
          validate_age(-1)
    assert print(str(exp_info.value)) == "age can not be less than zero"


def test_validate_age_invalid_age():
    with pytest.raises(ValueError , match= "age can not be less than zero"):
          validate_age(-1)
     












