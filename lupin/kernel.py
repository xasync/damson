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


def valid(**rules):
    def func(fn):
        def wrapper(*args, **kwargs):
            params = {}
            args_map = func_args_to_dict(fn, args)
            params.update(args_map)
            params.update(kwargs)
            validate_raise(params, **rules)
            return fn(*args, **kwargs)

        return wrapper

    return func
