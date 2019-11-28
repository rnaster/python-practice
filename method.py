"""
- class method
- static method

difference class method and static method
"""


class Demo:

    @classmethod
    def cls_mtd(*args):
        return args

    @staticmethod
    def stc_mtd(*args):
        return args


if __name__ == '__main__':
    print(Demo.cls_mtd())
    print(Demo.cls_mtd('hello'), '\n')
    print(Demo.stc_mtd())
    print(Demo.stc_mtd('hi'))
