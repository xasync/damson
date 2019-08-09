from lupin.constraint import Required


def test_require():
    assert Required()({'age': 18}, 'age')
