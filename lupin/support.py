import inspect


def func_args_to_dict(func, args):
    if not inspect.isfunction(func) or not isinstance(args, (list, tuple)):
        raise ValueError()
    varnames = func.__code__.co_varnames
    kvmap = {}
    for index, varname in enumerate(varnames):
        if index < len(args):
            kvmap[varname] = args[index]
    return kvmap
