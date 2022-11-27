class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        arr: list[int] = []

        last_sum: int = 0
        for n in nums:
            arr.append(n + last_sum)
            last_sum += n

        return arr
