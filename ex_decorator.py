"""
decorator test
"""
import time
import functools
import decorator as deco


@deco.register
def f1():
    print('running f1()')


@deco.register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', deco.registry)
    f1()
    f2()
    f3()


@deco.clock
def snooze(seconds):
    time.sleep(seconds)


@deco.clock
def factorial(n):
    return 1 if n < 2 else factorial(n - 1) * n


@deco.clock2
def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    tmp = power(a, b // 2)
    if b % 2:
        return tmp * tmp * a
    return tmp * tmp


@functools.lru_cache()
@deco.clock2
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    main()
    print('*' * 40, 'Calling snooze(.123)')
    snooze(0.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print(factorial.__name__)
    print('*' * 40, 'Calling power(2, 20)')
    print('2 ** 20! =', power(2, 20))
    print(power.__name__)
    print('*' * 40, 'Calling fibo(10)')
    print('fibonacci 20 =', fibo(20))
    print(fibo.__name__)
