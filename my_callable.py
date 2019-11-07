import random


def func(msg):
    print(msg)
    return


# user-defined callable object
class MyChoice:

    def __init__(self, a, b):
        self.values = [*range(a, b)]

    def choice(self):
        return random.choice(self.values)

    def __call__(self):
        return self.choice()


rand_num = MyChoice(1, 101)
print('My Callable object', *[rand_num() for _ in range(3)])
print(rand_num.choice.__name__)
print(rand_num.choice.__qualname__, '\n')

for obj in [13, str, random, func, MyChoice, rand_num]:
    print('%s is a callable object: %s' % (obj, callable(obj)))
