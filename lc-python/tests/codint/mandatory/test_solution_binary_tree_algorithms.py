from typing import List, Union

import pytest
from lc_python.codint.mandatory.binary_tree_algorithms.solution import Solution, TreeNode


@pytest.mark.parametrize(
    "values, targetSum, expected",
    [
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 1, 2),
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 2, 1),
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 3, 3),
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 5, 1),
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 6, 2),
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 7, 2),
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 13, 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 18, 2),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),
    ],
)
def test_path_sum_iii(values: List[Union[int, None]], targetSum: int, expected: int):
    nodes = [TreeNode(v) for v in values]
    for i, node in enumerate(nodes):
        left_i = 2 * i + 1
        right_i = 2 * i + 2
        if left_i < len(nodes) and nodes[left_i].val is not None:
            node.left = nodes[left_i]
        if right_i < len(nodes) and nodes[right_i].val is not None:
            node.right = nodes[right_i]
    root = nodes[0]
    returned = Solution().pathSum(root, targetSum)

    assert (
        expected == returned
    ), f"Wrong answer for tree {values} and targetSum {targetSum}. Expected: {expected}. Got: {returned}."
