class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Builds a table of n rows (1-indexed). We start by writing 0 in the 1st row.
        Now in every subsequent row, we look at the previous row and replace
        each occurrence of 0 with 01, and each occurrence of 1 with 10.

        Returns the k-th (1-indexed) symbol in the nth row of a table of n rows.
        """
        if n == 1:
            return 0

        mid = 2 ** (n - 2)
        if k > mid:
            return 1 if self.kthGrammar(n - 1, k - mid) == 0 else 0
        else:
            return self.kthGrammar(n - 1, k)
