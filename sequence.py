"""
list
mutable
variability

tuple
immutable list
record which have no field

unpacking
"""

tup = (123, 945, 9984194)
a, *b = tup
print('unpacking')
print(a)
print(b)

import collections

cards = collections.namedtuple('cards', 'rank suit')
card = cards(1, 'dia')
print('\nnamedtuple example')
print('rank: %s, suit: %s' % card)

print('\nadvanced slicing')
print('odd number')
print([*range(11)][1:11:2])
print('even number')
print([*range(11)][0:11:2])

print('\nnested list')
nested_list1 = [['_'] * 3 for _ in range(3)]
print('original list1', *nested_list1, sep='\n')
nested_list1[0][1] = '--'
print('modified list1', *nested_list1, sep='\n')

nested_list2 = [['_'] * 3] * 3
print('\noriginal list2', *nested_list2, sep='\n')
nested_list2[0][1] = '--'
print('modified list2', *nested_list2, sep='\n')

print('\nbisect')
import bisect
import random

my_list = []
for _ in range(7):
    num = random.randrange(15)
    bisect.insort(my_list, num)
    print('number: %d ->' % num, 'my_list:', my_list)

print('\npython array')
import time
from array import array

arr = array('d', (random.random() for _ in range(10 ** 7)))
s_time = time.time()
with open('floats.bin', 'wb') as f:
    arr.tofile(f)
print('elapsed time to write: %.4f' % (time.time() - s_time))

s_time = time.time()
arr2 = array('d')
with open('floats.bin', 'rb') as f:
    arr2.fromfile(f, 10 ** 7)
print('elapsed time to read: %.4f' % (time.time() - s_time))
print('arr is equivalent to arr2:', arr == arr2)

print('\nlist pop(0) vs collections.deque.popleft()')
lst = [*range(10 ** 5)]
s_time = time.time()
while lst:
    lst.pop(0)
print('elapsed time list pop(0): %.4f' % (time.time() - s_time))

dq = collections.deque(range(10 ** 5))
s_time = time.time()
while dq:
    dq.popleft()
print('elapsed time deque popleft(): %.4f' % (time.time() - s_time))
