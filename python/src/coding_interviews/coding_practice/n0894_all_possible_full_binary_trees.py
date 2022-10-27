from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cache = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        # Only odd number can generate a full Binary Tree.
        if N % 2 == 0:
            return []

        if N not in self.cache:
            result: List[TreeNode] = []

            # Step is 2 since we only want odd numbers.
            for i in range(1, N, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N - 1 - i):
                        result.append(TreeNode(0, left, right))

            self.cache[N] = result

        return self.cache[N]
