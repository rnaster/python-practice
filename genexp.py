"""
generator expression

memory utility
"""

# multiplication table, 1x1 ... 9x9
numbers = range(1, 10)
for a, b in ((num1, num2)
             for num1 in numbers
             for num2 in numbers):
    print('%d x %d: %d' % (a, b, a * b))
