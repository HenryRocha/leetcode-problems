from typing import List, Set


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result: Set[int] = set()
        previous: Set[int] = set()

        for i in arr:
            previous = {j | i for j in previous} | {i}
            result |= previous

        return len(result)
