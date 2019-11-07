def power(a, b=1):
    """
    a to the power of b, a^b
    :return: a ** b
    """
    if isinstance(a, tuple or list):
        a, b, *_ = a
    if b == 0:
        return 1
    if b == 1:
        return a
    tmp = power(a, b // 2)
    if b % 2 == 0:
        return tmp * tmp
    return tmp * tmp * a


# function as object
print(power(2, 9))
print(power.__name__)
print(type(power), '\n')
help(power)

# first-class function
my_power_func = power
print(my_power_func.__name__, '##')
print(my_power_func(2, 11))

# higher-order function, 'map'
print([*map(my_power_func, zip([2, 2, 2], [4, 8, 12]))])
