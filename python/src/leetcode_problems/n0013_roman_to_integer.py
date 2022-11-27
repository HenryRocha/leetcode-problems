class Solution:
    conversion_table: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        number: int = 0
        last_integer: int = 0

        for char in s[::-1]:
            current_integer = self.conversion_table[char]

            if current_integer >= last_integer:
                number += current_integer
            else:
                number -= current_integer

            last_integer = current_integer

        return number
