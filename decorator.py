"""
decorator
when compiling, f1 and f2 are decorated
"""
import time
registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked
