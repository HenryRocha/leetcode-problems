from typing import List


class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = i = 0
        result: List[str] = []
        for j, v in enumerate(s):
            count = count + 1 if v == "1" else count - 1
            if count == 0:
                result.append("1" + self.makeLargestSpecial(s[i + 1 : j]) + "0")
                i = j + 1
        return "".join(sorted(result, reverse=True))
