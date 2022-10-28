from collections import deque
from typing import Callable, TypeVar

import pytest
from _pytest.fixtures import SubRequest
from src.coding_interviews.interviews.interview_04.solution_01 import GraphNode
from src.coding_interviews.interviews.interview_04.solution_01 import has_route as has_route_s1

T = TypeVar("T")

HasRouteFuncType = Callable[[GraphNode[int], GraphNode[int]], bool]


@pytest.fixture(params=[has_route_s1])
def implementation(request: SubRequest) -> HasRouteFuncType:
    return request.param


class Graph:
    def __init__(self, adjacency: list[list[int]]):
        """
        adjacency: Adjacency matrix (must be square)
        """
        self.adj_matrix = adjacency
        n = len(adjacency)
        self.nodes = [GraphNode(i) for i in range(n)]
        for i, node in enumerate(self.nodes):
            node.adjacent = [
                self.nodes[j] for j, is_adjacent in enumerate(adjacency[i]) if is_adjacent and node != self.nodes[j]
            ]

    def __str__(self):
        return str(self.adj_matrix)


def ground_truth(adj: list[list[int]], origin: int, dst: int):
    n = len(adj)
    visited = [False for _ in range(n)]
    q = deque([origin])
    while q:
        i = q.popleft()
        for j in range(n):
            if not adj[i][j]:
                continue
            if j == dst:
                return True
            if not visited[j]:
                visited[j] = True
                q.append(j)
    return False


def _check(implementation: HasRouteFuncType, adj_mat: list[list[int]]):
    g = Graph(adj_mat)
    for i, origin in enumerate(g.nodes):
        for j, dst in enumerate(g.nodes):
            expected = ground_truth(adj_mat, i, j)
            received = implementation(origin, dst)
            assert expected == received, f"Didn't work for graph:\n{g}"


def test_1(implementation: HasRouteFuncType):
    _check(implementation, [[1]])


def test_2(implementation: HasRouteFuncType):
    _check(
        implementation,
        [
            [1, 0],
            [0, 1],
        ],
    )


def test_3(implementation: HasRouteFuncType):
    _check(
        implementation,
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ],
    )


def test_4(implementation: HasRouteFuncType):
    _check(
        implementation,
        [
            [1, 1, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 1],
        ],
    )


def test_5(implementation: HasRouteFuncType):
    _check(
        implementation,
        [
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        ],
    )
