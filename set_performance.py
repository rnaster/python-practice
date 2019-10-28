"""
set(dict) performance for 'in' operator
"""
import time


def experiment(exp, n):
    lst = [i for i in range(-500, 500)]
    set_ = {i for i in range(n)}
    s_time = time.time()
    found = 0
    for num in lst:
        if num in set_:
            found += 1
    print('n: %d, elasped time for exp %d: %.6f' % (n, exp, time.time() - s_time))
    return


if __name__ == '__main__':
    for exp, n in [(1, 1_000), (2, 10_000), (3, 100_000), (4, 1_000_000), (5, 10_000_000)]:
        experiment(exp, n)
