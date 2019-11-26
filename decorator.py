"""
decorator
when compiling, f1 and f2 are decorated
"""
import time
import functools

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


def register2(active=True):
    """
    parameterized decorator factory
    ex)
    @register2(active=True)
    def func(some_args):
        # something
        return
    """

    def real_deco(func):
        print('running register(active=%s) -> real_deco(%s)' % (active, func))
        if active:
            registry.append(func)
        return func

    return real_deco


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


def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked


def clock3(fmt='[{elapsed: 0.8f}s] {name}({args}) -> {result}'):
    """
    parameterized decorator factory
    """

    def real_deco(func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result

        return clocked

    return real_deco


if __name__ == '__main__':
    @clock3()
    def snooze(sec):
        time.sleep(sec)
        return sec


    for i in range(1, 2):
        snooze(i)
