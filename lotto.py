import random

from tombola import Tombola


class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable)
        self._randomizer = random.SystemRandom()

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        cls = type(self)
        if len(self._balls) < 1:
            raise LookupError('pick from empty %s' % cls.__name__)
        position = self._randomizer.randrange(len(self._balls))
        return self._balls.pop(position)

    def inspect(self):
        return tuple(sorted(self._balls))

    def __len__(self):
        return len(self._balls)

    def __call__(self):
        return self.pick()


if __name__ == "__main__":
    lotte = LotteryBlower(range(3))
    print(lotte.loaded())
    print(lotte.inspect())
