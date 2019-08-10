import lupin
from lupin.constraint import Required, DataType, Between
from lupin.exception import NotPassBetweenException, NotPassDataTypeException
import pytest


def test_validate():
    data = {'age': 18}
    flag, errors = lupin.validate(data, age=[Required(), Between(60, 100)])
    print flag, errors


def test_valid():
    @lupin.valid(a=[Required(), DataType(int), Between(1, 10)],
                 b=[Required(), DataType(int), Between(100, 1000, eopen=False)])
    def add(a, b):
        return a + b

    assert add(1, 100) == 101
    assert add(1, 1000) == 1001

    with pytest.raises(NotPassDataTypeException) as e:
        add(1.0, 100)

    with pytest.raises(NotPassBetweenException) as e:
        add(10, 1000)
