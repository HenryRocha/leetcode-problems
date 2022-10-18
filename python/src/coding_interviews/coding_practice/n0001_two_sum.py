from typing import Dict, List, Union


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        """
        sub_dict: Dict[int, int] = {}

        for i in range(len(nums)):
            sub: Union[int, None] = sub_dict.get(nums[i], None)
            if sub is None:
                sub_dict[target - nums[i]] = i
            else:
                return [sub, i]

        return []
