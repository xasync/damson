from exception import NotPassRequireException, NotPassDataTypeException, NotPassBetweenException


class Required(object):
    """
    Make a promise that the field must to be exist
    """

    def __call__(self, obj, name):
        flag = True if obj and obj[name] else False
        if not flag:
            raise NotPassRequireException(field=name, constraint='the field is required')
        return flag


class DataType(object):
    """
    Make a promise about the field's type in python.
    args: python's build-in types,likes: int/str/list and etc.
    """

    def __init__(self, *args):
        self.types = args

    def __call__(self, obj, name):
        if len(self.types) <= 0:
            return True
        if obj and obj[name]:
            flag = isinstance(obj[name], self.types)
            if not flag:
                raise NotPassDataTypeException(field=name, constraint='the type must be one of %s' % self.types)
            return flag
        else:
            return True


class Between(object):
    """
    Make a promise that the field's value is between the interval
    """

    def __init__(self, start, end, sopen=False, eopen=True):
        self.start = start
        self.end = end
        self.sopen = sopen
        self.eopen = eopen

    def __interval_str(self):
        return '{left}{start},{end}{right}'.format(
            left='(' if self.sopen else '[',
            start=self.start if self.start else 'N',
            end=self.end if self.end else 'N',
            right=')' if self.eopen else ']'
        )

    def __call__(self, obj, name):
        if obj and obj[name]:
            v = obj[name]
            left_flag = True
            right_flag = True
            if self.start:
                left_flag = v > self.start if self.sopen else v >= self.start
            if self.end:
                right_flag = v < self.end if self.eopen else v <= self.end

            if not left_flag or not right_flag:
                raise NotPassBetweenException(field=name, constraint=self.__interval_str())
            else:
                return True
