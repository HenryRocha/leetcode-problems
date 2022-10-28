import pytest
from src.coding_interviews.coding_practice.n0042_trapping_rain_water import SOLUTIONS


@pytest.fixture(params=SOLUTIONS)
def implementation(request):
    return request.param


def _check(heights, expected, solution: object):
    ret = solution().trap(heights)
    assert ret == expected, f"Wrong answer for input {heights}"


def test_1(implementation):
    _check([], 0, implementation)


def test_2(implementation):
    _check([0, 0, 0, 0, 0], 0, implementation)


def test_3(implementation):
    _check([0, 0, 100, 0, 0], 0, implementation)


def test_4(implementation):
    _check([10, 0, 100, 0, 10], 20, implementation)


def test_5(implementation):
    _check([10, 20, 100, 20, 10], 0, implementation)


def test_6(implementation):
    _check([100, 0, 0, 0, 0], 0, implementation)


def test_7(implementation):
    _check([0, 0, 0, 0, 10], 0, implementation)


def test_8(implementation):
    _check([100, 0, 0, 0, 10], 30, implementation)


def test_9(implementation):
    _check([10, 10, 10, 10, 100], 0, implementation)


def test_10(implementation):
    _check([20, 100, 0, 10, 0, 100, 10], 290, implementation)


def test_11(implementation):
    _check([20, 100, 90, 80, 90, 100, 10, 20, 15], 50, implementation)


def test_12(implementation):
    _check([200, 100, 90, 80, 90, 100, 10, 20, 150], 560, implementation)


def test_13(implementation):
    _check([199, 200, 100, 90, 80, 90, 100, 10, 20, 150, 142], 560, implementation)


def test_14(implementation):
    _check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, implementation)


def test_15(implementation):
    _check([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, implementation)
