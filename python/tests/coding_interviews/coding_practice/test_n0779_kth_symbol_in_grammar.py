from src.coding_interviews.coding_practice.n0779_kth_symbol_in_grammar import Solution


def _check(n: int, k: int, expected: int):
    ret = Solution().kthGrammar(n, k)
    assert ret == expected, f"Wrong answer for input {n}, {k}. Expected: {expected}. Returned: {ret}"


def test_1():
    _check(1, 1, 0)


def test_2():
    _check(2, 1, 0)


def test_3():
    _check(2, 2, 1)


def test_4():
    _check(3, 1, 0)


def test_5():
    _check(3, 2, 1)


def test_6():
    _check(3, 3, 1)


def test_7():
    _check(3, 4, 0)


def test_8():
    _check(4, 1, 0)


def test_9():
    _check(4, 2, 1)


def test_10():
    _check(30, 2**29, 1)


def test_11():
    _check(30, 2**20, 0)


def test_12():
    _check(30, 1, 0)


def test_13():
    _check(30, 15, 1)


def test_14():
    _check(20, 1024, 0)


def test_15():
    _check(10, 511, 0)
