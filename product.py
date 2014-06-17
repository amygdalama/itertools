import itertools


def product(*args):
    result = [[]]
    for arg in args:
        result = [prev + [x] for prev in result for x in arg]
    for prod in result:
        yield tuple(prod)


if __name__ == '__main__':
    result = product(range(7), range(2), range(5))
    expected = itertools.product(range(7), range(2), range(5))
    for exp, res in zip(expected, result):
        assert exp == res