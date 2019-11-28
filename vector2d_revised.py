"""
revised from vector2d.py

- __slot__
  - prevent dynamically property allocation
- property decorator for hash
  - hash return value: int
- __repr__ for dev
- __str__ for user
- class property
  - all instance have same property
- inheritance for class property modification
"""
import math

from array import array


class Vector:
    __slots__ = ('_x', '_y')
    type_code = 'd'

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.type_code)]) +
                bytes(array(self.type_code, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self._x, self._y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        comp = (format(c, format_spec) for c in coords)
        return outer_fmt.format(*comp)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @classmethod
    def from_bytes(cls, octets):
        type_code = chr(octets[0])
        memv = memoryview(octets[1:]).cast(type_code)
        return cls(*memv)

    def angle(self):
        return math.atan2(self.y, self.x)


class NewVector(Vector):
    """overriding for type_code"""
    type_code = 'f'
    pass


if __name__ == '__main__':
    v1 = Vector(3, 4)
    print(v1.x, v1.y)
    x, y = v1
    print((x, y), *v1)
    print(v1, repr(v1))
    print(bytes(v1))
    bytes_ = bytes(v1)
    print(Vector.from_bytes(bytes_), '\n')
    v2 = Vector(2, math.pi)
    print(format(v2))
    print(format(v2, '.3f'))
    print(v1, format(v1, '.3fp'))
    print(v2, format(v2, '.3fp'))
    v3 = Vector(12, 13)
    v4 = Vector(12, 13)
    print(v3 == v4, v3 is v4)
    print(hash(v3), hash(v4))
    print(v3.type_code, '#')
    print(repr(v3))
    v5 = NewVector(45, 32)
    print(repr(v5), type(v5), type(v5).__name__)
