"""
closure

the following class and two functions are same.
"""


class Average1:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series) / len(self.series)


def average2():
    series = []

    def average(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return average


def average3():
    total = 0
    count = 0

    def average(new_value):
        nonlocal total, count
        total += new_value
        count += 1
        return total / count

    return average


if __name__ == '__main__':
    avg1 = Average1()
    avg2 = average2()
    avg3 = average3()
    import random

    for _ in range(5):
        num = random.randint(0, 10)
        print('avg1: %.2f, avg2: %.2f, avg3: %.2f' % (avg1(num), avg2(num), avg3(num)))
