# conftest.py

import pytest
from ..myapp.sample import Student 
from datetime import datetime

@pytest.fixture
def dummy_student(request):
    return Student("meet" , datetime(2000 ,  1 ,1),"coe" , 20)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name , credits):
        return Student(name , datetime(2000 ,  1 ,1) , "coe" ,credits)
    return _make_dummy_student

