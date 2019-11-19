"""
decorator test
"""
import time
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


if __name__ == '__main__':
    main()
    print('*' * 40, 'Calling snooze(.123)')
    snooze(0.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))
    print(factorial.__name__)
