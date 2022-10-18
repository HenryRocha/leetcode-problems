from typing import Callable

import pytest
from src.coding_interviews.interviews.interview_01.solution_01 import one_edit_away as one_edit_away_s1
from src.coding_interviews.interviews.interview_01.solution_02 import one_edit_away as one_edit_away_s2


@pytest.fixture(params=[one_edit_away_s1, one_edit_away_s2])
def implementation(request):
    return request.param


def _check(s1, s2, is_one_edit_away, solution: Callable):
    ans1 = solution(s1, s2)
    ans2 = solution(s2, s1)
    msg1 = f'Did not work for strings "{s1}" and "{s2}"'
    msg2 = f'Did not work for strings "{s2}" and "{s1}"'
    if is_one_edit_away:
        assert ans1, msg1
        assert ans2, msg2
    else:
        assert not ans1, msg1
        assert not ans2, msg2


def test_example1(implementation):
    _check("pale", "ple", True, implementation)


def test_example2(implementation):
    _check("pales", "pale", True, implementation)


def test_example3(implementation):
    _check("pale", "bale", True, implementation)


def test_example4(implementation):
    _check("pale", "bake", False, implementation)


def test_example5(implementation):
    _check("bale", "pale", True, implementation)


def test_example6(implementation):
    _check("apple", "aple", True, implementation)


def test_example7(implementation):
    _check("apple", "aple", True, implementation)


def test_large(implementation):
    _check("abcdef", "abcdefghijklmnopqrstuvwxyz", False, implementation)


def test_palindrome(implementation):
    _check("fox", "xof", False, implementation)


def test_upper(implementation):
    _check("AbC", "abc", False, implementation)


def test_special1(implementation):
    _check("Happy?", "Happy!", True, implementation)


def test_special2(implementation):
    _check("Happy??", "Happy!!", False, implementation)
