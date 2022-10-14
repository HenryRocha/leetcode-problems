from typing import Optional, Union


class TreeNode:
    def __init__(
        self, val: Union[int, None] = 0, left: Union["TreeNode", None] = None, right: Union["TreeNode", None] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = {0: 1}

        def calculate(node: Union[TreeNode, None], current_sum: int, result: int) -> int:
            if not node:
                return result

            # Update current path's sum.
            current_sum += node.val if node.val is not None else 0
            # Update result, if there is a path in cache that adds up to target sum.
            result += cache.get(current_sum - targetSum, 0)
            # Update cache with the current path's sum.
            cache[current_sum] = cache.get(current_sum, 0) + 1

            result = calculate(node.left, current_sum, result)
            result = calculate(node.right, current_sum, result)
            cache[current_sum] -= 1

            return result

        return calculate(root, 0, 0)
