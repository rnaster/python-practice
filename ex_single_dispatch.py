"""
single dispatch

multiple data type
"""
from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<p>{0} (0x{0:x})</p>'.format(n)


@htmlize.register(abc.Sequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n</li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
    print(htmlize(abs))
    print(htmlize({1, 99, 3}))
    print(htmlize('asd & asdd * <br> qqq -;'))
    print()
    print(htmlize(('qwe', 66, (3, 4))))
    print(htmlize({'a': 3, 'b': 99}))
