"""
example of functools.partial
"""

from functools import partial
from operator import mul

# tag function
print(mul, '\n')

twice = partial(mul, 2)
print([*map(twice, range(11))])
