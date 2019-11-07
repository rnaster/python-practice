"""
'*': positional arguments
'**': keyword arguments
"""


def tag(name, *content, cls=None, **attrs):
    """generate multiple HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    attr_str = ''
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value in sorted(attrs.items()))
    if content:
        return '\n'.join('<%s%s>%s</%s>'
                         % (name, attr_str, c, name)
                         for c in content)
    return '<%s%s />' % (name, attr_str)


def func(a, b, *, c, d):
    """
    There are two methods to pass values into arguments of function.
    - positional argument
      func(1, 2)
    - keyword argument
      func(a=1, b=2)
    when passing value into "c, d",
    'func(a, b, *, c, d)' forces only one method by "passing keyword".
    """
    return a, b, c, d


if __name__ == '__main__':
    print(tag('br'))
    print(tag('p', 'hello'))
    print(tag('p', 'bye', cls='sidebar'))
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
              'src': 'sunset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))
    print()

    print(func(1, 3, c=4, d=99))
