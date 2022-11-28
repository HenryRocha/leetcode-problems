class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted([num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10])
        return int(digits[0] * 10 + digits[2]) + int(digits[1] * 10 + digits[3])
