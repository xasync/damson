# encoding:utf-8

import damson
from damson.constraint import DataType, Between


class ClassCase(object):

    @damson.verify(year=[DataType(int)],
                   month=[DataType(int), Between(1, 12, eopen=False)],
                   day=[DataType(int), Between(1, 31, eopen=False)])
    def date2str(self, year, month, day):
        return u'{year}-{month:02d}-{day:02d}'.format(year=year, month=month, day=day)
