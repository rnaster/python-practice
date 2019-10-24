import collections


class MyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, list):
            return self[tuple(key)]
        return []

    def get(self, key, default=None):
        return self.data.get(key, default)

    def __setitem__(self, key, value):
        if isinstance(key, list):
            self.data[tuple(key)] = value
        else:
            self.data[key] = value

    def __getitem__(self, key):
        if isinstance(key, list):
            key = tuple(key)
        if key in self.data:
            return self.data[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
        raise KeyError(key)


if __name__ == '__main__':
    d = MyDict()
    d[[1, 2]] = 3
    print(d[1])
    print(d.get(2))
    print(d.data)
    print(d[[2, 3]])
