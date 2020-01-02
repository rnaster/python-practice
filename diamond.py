"""
diamond problem
- multiple inheritance
"""


class SKT_T1:
    def ping(self):
        print('ping: %s' % type(self).__name__)


class SKT_T1_K(SKT_T1):
    def ping(self):
        print('SKT_K ping: %s' % type(self).__name__)

    def pong(self):
        print('pong: %s' % type(self).__name__)


class SKT_T1_S(SKT_T1):
    def pong(self):
        print('PONG: %s' % type(self).__name__)


class T1(SKT_T1_K, SKT_T1_S):
    def ping(self):
        super().ping()
        print('post-ping: %s' % type(self).__name__)

    def ping_pong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()


class SSW:
    def __init__(self, white):
        self.white = white


class SSB:
    def __init__(self, blue):
        self.blue = blue


class SSG(SSW, SSB):
    def __init__(self, w, b):
        SSW.__init__(self, w)
        SSB.__init__(self, b)

    def say(self):
        print('SamSung Galaxy', self.blue)


class GenG(SSG):
    def __init__(self, x, y):
        super().__init__(x, y)


if __name__ == '__main__':
    t1 = T1()
    t1.ping_pong()
    print()
    t1.ping()
    print()
    print(*T1.__mro__, sep='\n')
    print('#' * 10)
    super(T1, t1).pong()
    super(SKT_T1_K, t1).ping()
    print('*' * 10)
    gen_g = GenG(1, 2)
    gen_g.say()
