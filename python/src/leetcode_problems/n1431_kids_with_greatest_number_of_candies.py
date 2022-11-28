class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        return [candies[kid] + extraCandies >= max(candies) for kid in range(len(candies))]
