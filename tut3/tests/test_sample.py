import pytest
import sys
from tut3.myapp.sample import add 

@pytest.mark.skip(reason="mane man thayu")
def test_add():
    assert add(1,2) == 3

@pytest.mark.skipif(sys.version_info > (3,7) , reason="Use python 3.7 or Less")
def test_add_str():
    assert add("a" , "b") == "ab"


@pytest.mark.xfail(sys.platform == "linux"  ,  reason="Dont run on Linux")
def test_add_list():
    assert add([1],[2]) == [1,2]
    raise Exception()

   