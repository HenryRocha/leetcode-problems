from typing import List


class Solution01:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows: List[str] = [""] * numRows

        current_row: int = 0
        direction: int = 0  # 0 -> Down, 1 -> Up
        for char in s:
            rows[current_row] += char

            if direction == 0:
                current_row += 1
                if current_row == numRows:
                    direction = 1
                    current_row -= 2
            else:
                current_row -= 1
                if current_row == -1:
                    direction = 0
                    current_row += 2

        return "".join(rows)


SOLUTIONS: List[object] = [Solution01]
