# Link: https://leetcode.com/problems/longest-palindrome


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        seen = set()
        res = 0

        for index, c in enumerate(s):
            if c not in seen:
                seen.add(c)
            else:
                res += 2
                seen.remove(c)

        # There is still a character can be added to the palindrome.
        if len(seen) > 0:
            res += 1

        return res
