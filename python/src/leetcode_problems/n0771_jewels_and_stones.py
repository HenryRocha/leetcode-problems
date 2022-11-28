class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)

        total_jewels = 0
        for stone in stones:
            if stone in jewels_set:
                total_jewels += 1

        return total_jewels
