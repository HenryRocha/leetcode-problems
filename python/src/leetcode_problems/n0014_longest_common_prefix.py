class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = ""

        for chars in zip(*strs):
            if len(set(chars)) != 1:
                break
            else:
                longest += chars[0]

        return longest
