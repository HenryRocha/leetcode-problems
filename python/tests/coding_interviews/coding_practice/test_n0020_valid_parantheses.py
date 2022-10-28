from src.coding_interviews.coding_practice.n0020_valid_parantheses import Solution


def _check(s: str, expected: bool):
    ret = Solution().isValid(s)
    assert ret == expected, f'Wrong answer for input "{s}". Expected: {expected}. Returned: {ret}'


def test_1():
    _check("", True)


def test_2():
    _check("(", False)


def test_3():
    _check(")", False)


def test_4():
    _check(")(", False)


def test_5():
    _check("()", True)


def test_6():
    _check("(}", False)


def test_7():
    _check("())", False)


def test_8():
    _check("())(", False)


def test_9():
    _check("[({)}]", False)


def test_10():
    _check("[{()}]", True)


def test_11():
    _check("[{(){}}()]", True)


def test_12():
    _check("[]{()}[{()}]", True)
