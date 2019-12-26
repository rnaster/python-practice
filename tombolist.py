"""
Tombola abstract sub class
"""
import random

from tombola import Tombola


@Tombola.register
class TomboList(list):

    def pick(self):
        cls = type(self)
        if self:
            return self.pop(random.randrange(len(self)))
        else:
            raise LookupError('pop from empty %s' % cls.__name__)

    load = list.extend

    def loaded(self):
        return len(self) > 0

    def inspect(self):
        return tuple(sorted(self))


if __name__ == '__main__':
    ball = list(range(10))
    tombo_list = TomboList(ball)
    print(tombo_list, len(tombo_list))
    print(tombo_list.pick())
    print(TomboList.__mro__)
    print([*Tombola._abc_registry])
