"""
list comprehension
"""
import string
import time
import numpy as np

symbols = np.random.choice([*string.ascii_lowercase], 10, replace=False)
print('symbols:', symbols)
orders = []

print('for loop')
for sym in symbols:
    orders.append(ord(sym))
print(orders)

print('list comprehension')
orders = [ord(sym) for sym in symbols]
print(orders)

print('\nvariable scope in list comp')
x = 'ABC'
dummy = [ord(x) for x in x]
print('x:', x)
print(dummy)

print('\nmap vs list comp. speed')
arr = range(5_000_000)
s_time = time.time()
list(map(str, arr))
print('map elapsed time: %.4f' % (time.time() - s_time))

s_time = time.time()
[str(val) for val in arr]
print('list comp. elapsed time: %.4f' % (time.time() - s_time))

print('\ncartesian product')
colors = ['black', 'white', 'blue']
sizes = ['S', 'M', 'L', 'XL', 'XXL']
t_shirts = [(color, size)
            for color in colors
            for size in sizes]
print('T shirts')
print(*t_shirts, sep='\n')
