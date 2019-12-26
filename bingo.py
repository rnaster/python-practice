import random

from tombola import Tombola


class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        cls = type(self)
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty %s' % cls.__name__)

    def __len__(self):
        return len(self._items)

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(3))
    print(bingo.loaded())
    print(bingo.inspect())
    picks = []
    picks.append(bingo.pick())
    picks.append(bingo.pick())
    picks.append(bingo.pick())
    print(bingo.inspect(), bool(bingo))
