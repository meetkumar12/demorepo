# test_sample.py

import os
import json
from tut5.myapp.sample import save_dict



def test_dict_save(tmpdir):
    filepath = os.path.join(tmpdir , "test.json")
    _dict = {"a" : 1 , "b" : 2}

    save_dict(_dict, filepath)

    assert json.load(open(filepath , 'r')) == _dict

