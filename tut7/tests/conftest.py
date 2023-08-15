# conftest.py

import pytest
from ..myapp.sample import Student , get_topper
from datetime import datetime

@pytest.fixture(scope="function")
def dummy_student():
    print("Making Dummy Students")
    return Student("meet" , datetime(2000 ,  1 ,1), "coe" , 20)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name , credits):
        return Student(name , datetime(2000 ,  1 ,1) , "coe" ,credits)
    return _make_dummy_student
