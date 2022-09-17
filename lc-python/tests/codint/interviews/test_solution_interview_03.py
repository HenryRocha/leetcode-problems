from typing import Callable

import pytest
from lc_python.codint.interviews.interview_03.solution_01 import Stack
from lc_python.codint.interviews.interview_03.solution_01 import sort_stack as sort_stack_s1


@pytest.fixture(params=[sort_stack_s1])
def implementation(request):
    return request.param


def _check(values, solution: Callable):
    stack = Stack()
    stack._items = [v for v in values]
    solution(stack)

    msg = "Didn't work for the stack: {values}"
    assert stack._items == sorted(values, reverse=True), msg


def test_1(implementation):
    _check([], implementation)


def test_2(implementation):
    _check([1], implementation)


def test_3(implementation):
    _check(list(range(1, 11)), implementation)


def test_4(implementation):
    _check(list(range(10, 0, -1)), implementation)


def test_5(implementation):
    values = []
    for i in range(1, 11):
        values.append(i)
        values.append(10 - i + 1)
    _check(values, implementation)


def test_6(implementation):
    values = []
    for i in range(1, 11):
        for _ in range(5):
            values.append(i)
        for _ in range(5):
            values.append(10 - i + 1)
    _check(values, implementation)


def test_7(implementation):
    _check([1, 1, 1, 1, 1, 1, 1], implementation)


def test_8(implementation):
    _check([-1, -1, -1, -1, -1, -1, -1], implementation)


def test_9(implementation):
    values = []
    for i in range(1, 11):
        values.append(-(10 - i + 1))
        values.append(-i)
    _check(values, implementation)


def test_10(implementation):
    values = []
    for i in range(1, 11):
        for _ in range(5):
            values.append(-(10 - i + 1))
        for _ in range(5):
            values.append(-i)
    _check(values, implementation)
