from typing import Any, List


# DO NOT CHANGE THIS CLASS
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


# IMPLEMENT YOUR SOLUTION HERE (DO NOT CHANGE THE ARGUMENTS)
def sort_stack(stack: Stack) -> None:
    s1 = stack
    s2 = Stack()

    while not s1.is_empty():
        tmp = s1.pop()
        while not s2.is_empty() and s2.peek() > tmp:
            s1.push(s2.pop())
        s2.push(tmp)

    # At this point s1 should be empty,
    # so we need to move all items in s2
    # back to s1.
    while not s2.is_empty():
        s1.push(s2.pop())
