from src.coding_interviews.coding_practice.n0041_first_missing_positive import Solution


def _check(l: list[int], expected: int):
    ret = Solution().firstMissingPositive(l)
    assert ret == expected, f"Wrong answer for input {repr(l)}. Expected: {expected}. Returned: {ret}"


def test_1():
    _check([1], 2)


def test_2():
    _check([10], 1)


def test_3():
    _check([3, 2, 1, 4, -1, 9, 7, -1, 5, 8, 6], 10)


def test_4():
    _check([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)


def test_5():
    _check([1, 3], 2)


def test_6():
    _check([2, 3], 1)


def test_7():
    _check([-1, -2, -3], 1)


def test_8():
    _check([1, 2, 0], 3)


def test_9():
    _check([3, 4, -1, 1], 2)


def test_10():
    _check([7, 8, 9, 11, 12], 1)
