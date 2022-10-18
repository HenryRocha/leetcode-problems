class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def nth_to_last(head, k: int):
    length = 0
    current = head
    while current is not None:
        current = current.next
        length += 1

    current = head
    for i in range(length):
        if length - i == k:
            return current
        else:
            current = current.next

    return None
