"""
function introspection
"""
from clip import clip
from argument import func
from inspect import signature
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split


def print_params(f):
    print('%s params' % f.__name__)
    for name, param in signature(f).parameters.items():
        print(param.kind, ':', name, '=', param.default)
    print()
    return


if __name__ == '__main__':
    print_params(clip)
    print_params(func)
    print_params(train_test_split)
    print_params(TSNE)
