class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)

        tmp: set[str] = set()
        current_biggest = 0
        left_ptr = 0
        right_ptr = 0

        while right_ptr < size:
            if s[right_ptr] not in tmp:
                # Add character to set and move right pointer to the right.
                tmp.add(s[right_ptr])
                right_ptr += 1
            else:
                # Update current state if we've found a longer substring.
                current_biggest = max(len(tmp), current_biggest)
                tmp = set()

                # Move left pointer to the right until we hit the first
                # appearance for right pointer's character.
                for i in range(left_ptr, right_ptr):
                    if s[i] == s[right_ptr]:
                        left_ptr = i + 1
                        right_ptr = i + 1
                        tmp = set()
                        break

        return max(len(tmp), current_biggest)
