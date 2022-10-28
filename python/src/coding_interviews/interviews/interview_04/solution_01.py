from typing import Generic, List, Optional, Set, TypeVar

T = TypeVar("T")


class GraphNode(Generic[T]):
    def __init__(self, value: Optional[T] = None):
        self.value = value
        self.adjacent: List["GraphNode"[T]] = []  # List of Nodes this node points to


def has_route(start_node: GraphNode[T], end_node: GraphNode[T]) -> bool:
    """
    Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
    """
    if start_node == end_node:
        return True

    visited: Set[GraphNode[T]] = set()

    stack = [start_node]
    while stack:
        curr = stack.pop()

        if curr not in visited:
            visited.add(curr)

            if curr == end_node:
                return True

            for node in curr.adjacent:
                stack.append(node)

    return False
