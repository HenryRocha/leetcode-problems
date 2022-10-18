from typing import List


class Solution01:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given matrix by 90 degrees (clockwise), in-place.
        """
        # Transpose the matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for row in matrix:
            row.reverse()


SOLUTIONS: List[object] = [Solution01]
