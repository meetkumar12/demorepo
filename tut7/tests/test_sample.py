# test_sample.py

from ..myapp.sample import Student , get_topper
import pytest
from datetime import datetime




def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20

def test_get_topper(make_dummy_student):
    students =[
        make_dummy_student("Ram" , 21),
        make_dummy_student("shyam" , 22),
        make_dummy_student("Ravi" , 24)
    ] 


    topper = get_topper(students)

    assert topper == students[2]


    