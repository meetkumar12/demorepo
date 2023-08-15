from tut1.myapp.sample import add , multi

def test_add():
    assert add(1,2) == 3

def test_add_str():
    assert add("a" , "b") == "ab"


def test_multi():
    assert multi(5 ,5) == 25


def test_add_num():
     assert add(4,4) == 8

def test_multi_num():
    assert multi(5,6) == 30    