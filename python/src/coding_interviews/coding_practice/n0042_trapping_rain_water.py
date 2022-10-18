from typing import List


class Solution01:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        max_idx = length - 1

        max_water: List[int] = [0] * length
        for i in range(length):
            if i == 0 or i == max_idx:
                max_water[i] = 0
                continue

            # Calculate max to the left of the current height.
            max_left = max(height[:i])
            # Calculate max to the right of the current height.
            max_right = max(height[i:])

            # Calculate how many blocks of water can sit on top of
            # the current height.
            max_water[i] = max(min(max_left, max_right) - height[i], 0)

        return sum(max_water)


class Solution02:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        max_idx = length - 1

        # Calculate the max height on the left of each
        # item in the heights list.
        max_left: List[int] = []
        for i in range(length):
            if i == 0:
                max_left.append(0)
            else:
                left = height[i - 1]
                last = max_left[i - 1]
                max_left.append(max(left, last))

        # Calculate the max height on the right of each
        # item in the heights list.
        max_right: List[int] = [0] * length
        for i in range(length - 1, -1, -1):
            if i == max_idx:
                max_right[i] = 0
            else:
                right = height[i + 1]
                last = max_right[i + 1]
                max_right[i] = max(right, last)

        # Calculate how much water can sit on top of each
        # item in the list.
        max_water: List[int] = []
        for i in range(length):
            max_water.append(max(min(max_left[i], max_right[i]) - height[i], 0))

        return sum(max_water)


class Solution03:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left_idx: int = 0
        right_idx: int = len(height) - 1
        left_max: int = height[0]
        right_max: int = height[-1]
        total_water_blocks: int = 0

        while left_idx < right_idx:
            if left_max < right_max:
                left_idx += 1
                left_max = max(left_max, height[left_idx])
                total_water_blocks += left_max - height[left_idx]
            else:
                right_idx -= 1
                right_max = max(right_max, height[right_idx])
                total_water_blocks += right_max - height[right_idx]

        return total_water_blocks


SOLUTIONS: List[object] = [Solution01, Solution02, Solution03]
