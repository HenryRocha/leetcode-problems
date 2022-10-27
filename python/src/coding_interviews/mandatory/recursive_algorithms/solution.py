from typing import Any, Generic, Iterable, List, Tuple, TypeVar, Union

T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, value: Union[T, None] = None):
        self.value = value
        self.left: Union["TreeNode"[T], None] = None
        self.right: Union["TreeNode"[T], None] = None


class Tree(Generic[T]):
    def __init__(self, representation: Iterable[T]):
        """
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        """
        if not representation:
            self.root = None
            return

        nodes: List[TreeNode[T]] = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            if node is not None:
                nodes.append(node)
        self.root = nodes[0]


class LinkedListNode(Generic[T]):
    def __init__(self, value: T, next_node: Any = None):
        self.value = value
        self.next: Union["LinkedListNode"[T], None] = next_node


class LinkedList(Generic[T]):
    def __init__(self, values: Iterable[T]):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node

    def __iter__(self):
        node = self.root
        while node:
            yield node.value
            node = node.next


# Implement the functions below


def list_sum(l: list[int]) -> int:
    if not l:
        return 0

    return l.pop() + list_sum(l)


def digit_sum(n: int) -> int:
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)


def tree_sum(root: Union[TreeNode[int], None]) -> int:
    if root is None:
        return 0

    current = root.value if root.value is not None else 0
    return current + tree_sum(root.left) + tree_sum(root.right)


def tree_max(root: Union[TreeNode[int], None]) -> float:
    if root is None:
        return -float("inf")

    current = root.value if root.value is not None else 0
    return max(current, tree_max(root.left), tree_max(root.right))


def k_combinations(l: list[int], k: int) -> list[list[int]]:
    if k == 0:
        return [[]]
    elif len(l) == 0:
        return []

    return k_combinations(l[1:], k) + [[l[0]] + comb for comb in k_combinations(l[1:], k - 1)]


def all_strictly_increasing_sequences(k: int, n: int, **kwargs: Any) -> list[list[int]]:
    """
    Returns all strictly increasing sequences of length k such that
    all elements belong to the first n natural numbers. This is done
    recursively.

    Example: for k=1 and n=4 it returns [[1], [2], [3], [4]]
    Example: for k=2 and n=3 it returns [[1,2], [1,3], [2,3]]
    Example: for k=3 and n=3 it returns [[1,2,3]]
    Example: for k=3 and n=4 it returns [[1,2,3], [1,3,4], [2,3,4]]
    """
    if k == 0:
        return [[]]
    elif n == 0:
        return []

    result = all_strictly_increasing_sequences(k, n - 1, first=False) + [
        [n] + comb for comb in all_strictly_increasing_sequences(k - 1, n - 1, first=False)
    ]
    result = [sorted(comb) for comb in result] if kwargs.get("first", None) is None else result
    return result


def create_pattern(n: int) -> list[int]:
    if n <= 0:
        return [n]

    return [n] + create_pattern(n - 5) + [n]


def find_middle(head: LinkedListNode[T]) -> LinkedListNode[T]:
    # Don't change this function
    return find_middle_rec(head)[1]


def find_middle_rec(head: LinkedListNode[T], n: int = 0) -> Tuple[int, LinkedListNode[T]]:
    """
    Returns the node in the middle of the linked list. If the list has an even
    number of elements, the second of the two middle elements is returned.

    Example: for the list [1,2,3,4,5] it returns the node with value 3
    Example: for the list [1,2,3,4,5,6] it returns the node with value 4

    This is done recursively.
    """
    if head is None or head.next is None:
        return 1, head

    m, node = find_middle_rec(head.next, n + 1)
    return m + 1, head if m == n or m == n - 1 else node
