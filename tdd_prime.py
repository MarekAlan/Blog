import pytest


def prime(n):
    lst = []
    d = 2
    while n > 1:
        while n % d == 0:
            lst.append(d)
            n = n / d
        d += 1
    return lst


@pytest.mark.parametrize('n, result', [
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (5, [5]),
    (6, [2, 3]),
    (7, [7]),
    (8, [2, 2, 2]),
    (9, [3, 3]),
    (2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 7 * 11, [2, 2, 2, 2, 3, 3, 5, 7, 7, 11]),
])
def test_prime(n, result):
    assert prime(n) == result
