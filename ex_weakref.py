"""
weak reference
"""
import weakref


class Color:

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return 'Color(%s)' % self.color


if __name__ == "__main__":
    a_set = {0, 1}
    wref = weakref.ref(a_set)
    print('weak ref', wref())
    a_set = {1, 2, 3}
    print('weak ref is dead:', wref() is None)

    stock = weakref.WeakValueDictionary()
    catalog = [Color('red'), Color('blue'), Color('yellow'),
               Color('black'), Color('green')]
    for color in catalog:
        print(color)
        stock[color.color] = color
    del catalog
    print(*stock.items(), sep='\n')
