"""
My Abstract Base Class : Tombola
"""
import abc

from abc import abstractmethod


class Tombola(abc.ABC):

    @abstractmethod
    def load(self, iterable):
        """add iterable object"""
        pass

    @abstractmethod
    def pick(self):
        """if not empty pop randomly otherwise raise LookupError"""
        pass

    @abstractmethod
    def __len__(self):
        pass

    def loaded(self):
        """if not empty True otherwise False"""
        return len(self) > 0

    def inspect(self):
        """return every items"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
