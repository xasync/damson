class Validator:
    def __init__(self):
        self.message = None

    def validate(self, obj, name):
        return True

    def result(self):
        return self.message


class Required(Validator):
    """
    Make a promise that the field must to be exist
    """

    def validate(self, obj, name):
        flag = True if obj and obj[name] else False
        if not flag:
            self.message = '"%s" is required, but do not find it in object.' % (name)
        return flag


class DataType(Validator):
    """
    Make a promise about the field's type in python.
    args: python's build-in types,likes: int/str/list and etc.
    """

    def __init__(self, *args):
        Validator.__init__(self)
        self.types = args

    def validate(self, obj, name):
        if len(self.types) <= 0:
            return True
        if obj and obj[name]:
            flag = isinstance(obj[name], self.types)
            if not flag:
                self.message = '"%s" is wrong data type and requires %s' % (name, self.types)
            return flag
        else:
            return True


class Between(Validator):
    """
    Make a promise about the field's type in python.
    args: python's build-in types,likes: int/str/list and etc.
    """

    def __init__(self, start, end, sopen=False, eopen=True):
        Validator.__init__(self)
        self.start = start
        self.end = end
        self.sopen = sopen
        self.eopen = eopen

    def validate(self, obj, name):
        if obj and obj[name]:
            v = obj[name]

            flag = (v > self.start if self.sopen else v >= self.start) and (
                v < self.end if self.eopen else v <= self.end)
            if not flag:
                self.message = '"%s" is not between %s%s,%s%s' % (name,
                                                                  '(' if self.sopen else '[',
                                                                  self.start, self.end,
                                                                  ')' if self.eopen else ']')
                return flag
            else:
                return True
