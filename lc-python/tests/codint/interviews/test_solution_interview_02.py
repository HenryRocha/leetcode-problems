from typing import Callable

import pytest
from lc_python.codint.interviews.interview_02.solution_01 import nth_to_last as nth_to_last_s1
from lc_python.codint.interviews.interview_02.solution_02 import nth_to_last as nth_to_last_s2


@pytest.fixture(params=[nth_to_last_s1, nth_to_last_s2])
def implementation(request):
    return request.param


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def make_list(l: list) -> list[Node]:
    nodes = [Node(v) for v in l]
    for node, next in zip(nodes[:-1], nodes[1:]):
        node.next = next
    return nodes


def strlist(node: Node) -> str:
    s = []
    while node:
        s.append(str(node.value))
        node = node.next
    return "->".join(s) or "Empty"


def check(values: list, k: int, solution: Callable):
    head = None
    expected = None
    if values:
        l = make_list(values)
        head = l[0]
        if k <= len(l):
            expected = l[-k]
    ans = solution(head, k)

    msg = f"Didn't work for list '{strlist(head)}' and k={k}"
    assert expected == ans, msg


def test_1(implementation):
    check(None, 10, implementation)


def test_2(implementation):
    check([1, 1, 1, 1, 1, 1], 3, implementation)


def test_3(implementation):
    check(range(1, 11), 1, implementation)


def test_4(implementation):
    check(range(1, 11), 10, implementation)


def test_5(implementation):
    check(range(1, 11), 20, implementation)


def test_6(implementation):
    check(range(1, 11), 2, implementation)


def test_7(implementation):
    check(range(1, 11), 3, implementation)


def test_8(implementation):
    check(range(1, 11), 4, implementation)


def test_9(implementation):
    check(range(1, 11), 5, implementation)


def test_10(implementation):
    check(range(1, 11), 6, implementation)
