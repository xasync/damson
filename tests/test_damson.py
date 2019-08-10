from __future__ import print_function
import damson
from damson.constraint import Required, DataType, Between
from damson.exception import NotPassBetweenException, NotPassDataTypeException
import pytest


def test_validate():
    data = {'age': 18}
    flag, errors = damson.validate(data, age=[Required(), Between(60, 100)])
    print(flag, errors)


def test_verify():
    @damson.verify(a=[Required(), DataType(int), Between(1, 10)],
                   b=[Required(), DataType(int), Between(100, 1000, eopen=False)])
    def add(a, b):
        return a + b

    assert add(1, 100) == 101
    assert add(1, 1000) == 1001

    with pytest.raises(NotPassDataTypeException) as e:
        add(1.0, 100)
        assert 'NotPassDataTypeException' in str(e)

    with pytest.raises(NotPassBetweenException) as e:
        add(10, 1000)
        assert 'NotPassBetweenException' in str(e)

    @damson.verify(**{'name': [Required(), DataType(str)], '1': [Required(), DataType(int)]})
    def mix_args(name, *args):
        return '%s=%s' % (name, args)

    mix_args('stone', 10, 20, 30)

    @damson.verify(**{'0': [Required(), DataType(str)], '1': [Required(), DataType(int)]})
    def create_kv(*args):
        key = args[0]
        value = args[1]
        return {key: value}

    kv = create_kv('name', 10)
    assert kv['name'] == 10


def test_package():
    print(damson.__version__)
