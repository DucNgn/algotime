class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Time: O(n)
        Space: O(1)
        """
        slow, fast = 0, 0
        while fast < len(nums):
            nums[slow] = nums[fast]
            if nums[slow] != 0:
                slow += 1
            fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1
