from typing import Callable

import pytest
from src.coding_interviews.interviews.interview_05.solution_01 import swap_odd_even_bits as swap_odd_even_bits_s1


@pytest.fixture(params=[swap_odd_even_bits_s1])
def implementation(request):
    return request.param


def _check(n_bin, expected_bin, solution: Callable):
    n = int(n_bin, base=2)
    expected = int(expected_bin, base=2)
    received = solution(n)

    msg = f"Wrong answer for {n:b}. Expected: {expected:b}. Got: {received:b}."
    assert expected == received, msg


def test_1(implementation):
    a = "00000000000000000000000000000000"
    b = "00000000000000000000000000000000"
    _check(a, b, implementation)
    _check(b, a, implementation)


def test_2(implementation):
    a = "10101010101010101010101010101010"
    b = "01010101010101010101010101010101"
    _check(a, b, implementation)
    _check(b, a, implementation)


def test_3(implementation):
    a = "11100011100011100011100011100011"
    b = "11010011010011010011010011010011"
    _check(a, b, implementation)
    _check(b, a, implementation)


def test_4(implementation):
    a = "10011001100110011001100110011001"
    b = "01100110011001100110011001100110"
    _check(a, b, implementation)
    _check(b, a, implementation)


def test_5(implementation):
    a = "11111111111111111111111111111111"
    b = "11111111111111111111111111111111"
    _check(a, b, implementation)
    _check(b, a, implementation)
