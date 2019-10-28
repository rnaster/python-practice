"""
immutable mapping
"""

from types import MappingProxyType

print('assign key-value to ex_dict')
ex_dict = {'a': 1, 'b': 2}
print(ex_dict)
immutable_dict = MappingProxyType(ex_dict)
print('\nimmutable dictionary')
print(immutable_dict)

print('\nassign new key-value to immutable_dict')
try:
    immutable_dict['c'] = 3
except TypeError as error:
    print(error)

print('\nassign new key-value to ex_dict')
ex_dict['c'] = 3
print('immutable dictionary')
print(immutable_dict)
