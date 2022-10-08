# Link: https://leetcode.com/problems/move-zeroes


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = []
        pop_idx = 0

        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1

        return len(stack) == 0
