from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique_integers = set(nums)
        data = (n for n in range(1, len(unique_integers) + 2) if n not in unique_integers)
        return min(data)
