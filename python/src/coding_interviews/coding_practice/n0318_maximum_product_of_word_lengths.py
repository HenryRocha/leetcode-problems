from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        length = len(words)
        char_sets = [set(word) for word in words]
        max_product = 0

        for i in range(length):
            for j in range(i + 1, length):
                if not (char_sets[i] & char_sets[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))

        return max_product
