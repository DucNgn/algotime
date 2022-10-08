# Link: https://leetcode.com/problems/intersection-of-two-arrays


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """
        res = set()
        nums1 = set(nums1)
        for i, elm in enumerate(nums2):
            if elm in nums1:
                res.add(elm)

        return list(res)
