from src.coding_interviews.coding_practice.n0761_special_binary_string import Solution


def _check(s: str, expected: str):
    ret = Solution().makeLargestSpecial(s)
    assert ret == expected, f'Wrong answer for input "{s}". Expected: {expected}. Returned: {ret}.'


def test_1():
    _check("", "")


def test_2():
    _check("10", "10")


def test_3():
    _check("1010", "1010")


def test_4():
    _check("1100", "1100")


def test_5():
    _check("101100", "110010")


def test_6():
    _check("101010", "101010")


def test_7():
    _check("110010", "110010")


def test_8():
    _check("111000", "111000")


def test_9():
    _check("11011000", "11100100")


def test_10():
    _check("1101011000", "1110010100")


def test_11():
    _check("111110001110010000", "111110010011100000")


def test_12():
    _check("111110001110010000111110001110010000", "111110010011100000111110010011100000")


def test_13():
    _check("111110001110010000111110010011100000", "111110010011100000111110010011100000")


def test_14():
    _check("11111000101110010000111110010011100000", "11111001001110001000111110010011100000")
