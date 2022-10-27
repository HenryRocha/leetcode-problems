from src.coding_interviews.coding_practice.n0318_maximum_product_of_word_lengths import Solution


def _check(l: list[str], expected: int):
    ret = Solution().maxProduct(l)
    assert ret == expected, f"Wrong answer for input {repr(l)}. Expected: {expected}. Returned: {ret}"


def test_1():
    _check([], 0)


def test_2():
    _check([""], 0)


def test_3():
    _check(["abcde"], 0)


def test_4():
    _check(["aa", "bcdef"], 10)


def test_5():
    _check(["aa", "abcdef"], 0)


def test_6():
    _check(["abcdef", "fgh", "hijk", "klmnopa"], 24)


def test_7():
    _check(["abcdef", "bcdefghi", "fghijk", "ijklmn", "lmnopqr"], 56)


def test_8():
    _check(["abcdef", "bcdefghi", "aaaaaaaaaaaaaaa", "fghijk", "ijklmn", "bbbbbbbbbbbbbb", "lmnopqr"], 210)


def test_9():
    _check(["a", "aa", "aaa", "aaaa", "abbbbbbbb", "bbb", "c"], 12)


def test_10():
    _check(["bbbbbbbac", "aaaabc", "cccccccba"], 0)
