from __future__ import print_function
from damson.constraint import NotPassRequireException


def test_require():
    try:
        raise NotPassRequireException('the field must be exist')
    except Exception as e:
        print(e)
