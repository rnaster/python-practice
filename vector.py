"""
n-dim vector class

- restricted attribute assignment
- collapse string using 'reprlib'
- return Vector class after slicing
- angle method
  - https://en.wikipedia.org/wiki/N-sphere#Spherical_coordinates
"""
import functools
import itertools
import math
import numbers
import operator
import reprlib

from array import array


class Vector:
    type_code = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.type_code, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['): -1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.type_code)]) +
                bytes(self._components))

    def __eq__(self, other):
        return len(self) == len(other) \
               and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        initial = 0
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, initial)

    def __abs__(self):
        return math.sqrt(sum(val * val for val in self))

    def __bool__(self):
        return bool(abs(self))

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        msg = '{cls.__name__} indices must be integers'
        raise TypeError(msg.format(cls=cls))

    def __len__(self):
        return len(self._components)

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            error = ''
            if name in cls.shortcut_names:
                error = 'read only attribute {attr_name!r}'
            elif name.islower():
                error = 'can`t set attributes "a" to "z" in {cls_name!r}'
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __format__(self, format_spec=''):
        coords = self
        outer_format = '({})'
        if format_spec.endswith('h'):
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_format = '<{}>'
        components = (format(c, format_spec) for c in coords)
        return outer_format.format(', '.join(components))

    def angle(self, n):
        magnitude = math.sqrt(sum(comp * comp for comp in self[n:]))
        angle = math.atan2(magnitude, self[n - 1])
        if n == len(self) - 1 and self[-1] < 0:
            return 2 * math.pi - angle
        return angle

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    @classmethod
    def from_bytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(memv)


if __name__ == '__main__':
    a = Vector([1, 2, 3])
    print(a)
    b = Vector((2, 3, 4.0))
    print(b)
    c = Vector(range(10))
    print(repr(c))
    print(len(c))
    print(type(c))
    print(c[1:4])
    print(c.z, '##')
    c.xx = 123
    print(c.xx, c)
