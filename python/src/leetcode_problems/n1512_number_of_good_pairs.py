class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        good_pairs: int = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1

        return good_pairs
