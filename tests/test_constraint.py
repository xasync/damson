import pytest
from lupin.constraint import Required, DataType, Between
from lupin.exception import (NotPassRequireException, NotPassDataTypeException, NotPassBetweenException,
                             WrongIntervalException)


def test_require():
    data = {'age': 18}
    assert Required()(data, 'age')

    with pytest.raises(NotPassRequireException) as e:
        Required()(data, 'name')
        assert 'NotPassRequireException' in str(e)


def test_data_type():
    data = {'age': 18, 'name': 'stone', 'man': True, 'salary': 7500.10, 'hobbies': ['basketball', 'sing'],
            'feature': {'test': True}, 'seq': (23, 345)}

    assert DataType(int)(data, 'age')
    assert DataType(str)(data, 'name')
    assert DataType(bool)(data, 'man')
    assert DataType(float)(data, 'salary')
    assert DataType(list)(data, 'hobbies')
    assert DataType(dict)(data, 'feature')
    assert DataType(tuple)(data, 'seq')

    with pytest.raises(NotPassDataTypeException) as e:
        DataType(int)(data, 'salary')
        assert 'NotPassDataTypeException' in str(e)


def test_between():
    data = {'age': 18}
    assert Between(1)(data, 'age')
    assert Between(1, 20)(data, 'age')

    with pytest.raises(WrongIntervalException) as e:
        Between(100, 10)(data, 'age')

    with pytest.raises(NotPassBetweenException) as e:
        Between(60)(data, 'age')
