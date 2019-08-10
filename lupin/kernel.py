import inspect
from exception import LupinException
from constraint import LupinConstraint
from support import func_args_to_dict


def validate(obj, **kwargs):
    if not isinstance(obj, dict):
        raise LupinException('the argument of validate function must to be a dict.')
    errors = []
    if len(kwargs) <= 0:
        return True, errors
    for field, rules in kwargs.iteritems():
        if len(rules) <= 0:
            continue
        for rule in rules:
            try:
                if isinstance(rule, LupinConstraint):
                    rule(obj, field)
            except Exception as e:
                errors.append(str(e))
    return len(errors) <= 0, errors


def validate_raise(obj, **kwargs):
    if not isinstance(obj, dict):
        raise LupinException('the argument of validate function must to be a dict.')
    if len(kwargs) <= 0:
        return True
    for field, rules in kwargs.iteritems():
        if len(rules) <= 0:
            continue
        for rule in rules:
            if isinstance(rule, LupinConstraint):
                rule(obj, field)
    return True


def verify(**rules):
    """
    This decoration wrapper is used to check the arguments of function. If the arguments does not match rules, it will
    throw exception. you can use it likes:

    import lupin
    from lupin.constraint import DataType

    @lupin.verify(a=[DataType(int)],b=[DataType(int)])
    def add(a,b):
        return a+b

    add(2,3)   # 5
    add(2,3.0) # throws exception

    :param rules: declares the constraint
    :return: result
    """

    def func(fn):
        def wrapper(*args, **kwargs):
            if inspect.isfunction(fn):
                params = {}
                args_map = func_args_to_dict(fn, args)
                params.update(args_map)
                params.update(kwargs)
                validate_raise(params, **rules)
            else:
                print 'Abort to execute validation, because that it just only apply on function'
            return fn(*args, **kwargs)

        return wrapper

    return func
