from lupin.constraint import NotPassRequireException


def test_require():
    try:
        raise NotPassRequireException('the field must be exist')
    except Exception as e:
        print e
