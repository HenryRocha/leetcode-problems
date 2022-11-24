from src.coding_interviews.coding_practice.n0045_jump_game_2 import Solution


def _check(l: list[int], expected: int):
    ret = Solution().jump(l)
    assert ret == expected, f"Wrong answer for input {repr(l)}. Expected: {expected}. Returned: {ret}"


def test_1():
    _check([], 0)


def test_2():
    _check([1], 0)


def test_3():
    _check([1, 1], 1)


def test_4():
    _check([1, 1, 1], 2)


def test_5():
    _check([10, 0, 0, 0, 1], 1)


def test_6():
    _check([4, 10, 1, 1, 1, 1, 1, 1], 2)


def test_7():
    _check([4, 1, 5, 1, 1, 1, 1, 1, 1], 3)


def test_8():
    _check([5, 1, 1, 10, 1, 1, 1, 1, 1], 2)


def test_9():
    _check([5, 0, 0, 10, 0, 0, 0, 0, 1], 2)


def test_10():
    _check([3, 3, 2, 1, 1, 1, 4, 2, 2, 4, 1, 2, 2, 1], 6)
