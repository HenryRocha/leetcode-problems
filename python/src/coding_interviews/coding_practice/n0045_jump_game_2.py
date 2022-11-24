from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        jumps = 0
        while r < len(nums) - 1:
            jumps += 1
            furthest = max([i + nums[i] for i in range(l, r + 1)])
            l, r = r + 1, furthest

        return jumps
