class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        arr: list[int] = []

        for i in range(len(nums) - n):
            arr.append(nums[i])
            arr.append(nums[i + n])

        return arr
