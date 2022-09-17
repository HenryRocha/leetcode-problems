from typing import Tuple


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def nth_to_last_and_count(head: Node, k: int) -> Tuple[int, Node | None]:
    """
    Returns the position of the node from end to start and
    the node in the k-th position, if it has already been reached.
    """
    if head == None:
        return (1, None)
    else:
        idx, node = nth_to_last_and_count(head.next, k)
        if idx == k:
            return (idx + 1, head)
        else:
            return (idx + 1, node)


def nth_to_last(head: Node, k: int) -> Node:
    return nth_to_last_and_count(head, k)[1]
