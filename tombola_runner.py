import doctest
import bingo, lotto, tombolist

from tombola import Tombola

TEST_FILE = 'tombola_tests.rst'
TEST_MSG = '{0:16} {1.attempted:2} tests, {1.failed:2} failed - {2}'


def main():
    real_sub = Tombola.__subclasses__()
    virtual_sub = [*Tombola._abc_registry]

    for cls in real_sub + virtual_sub:
        test(cls)
    return


def test(cls):
    res = doctest.testfile(
        TEST_FILE,
        globs={'ConcreteTombola': cls},
        optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
    )
    tag = 'Fail' if res.failed else 'OK'
    print(TEST_MSG.format(cls.__name__, res, tag))
    return


if __name__ == "__main__":
    main()
