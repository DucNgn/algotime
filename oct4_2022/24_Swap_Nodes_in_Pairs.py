# Link: https://leetcode.com/problems/swap-nodes-in-pairs

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach
        Time: O(n)
        Space: O(n)
        """
        if not head:
            return None
        next_node = head.next
        if not next_node:
            return head
        head.next, next_node.next = self.swapPairs(next_node.next), head
        return next_node


class Solution_2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach
        Time: O(n)
        Space: O(1)
        """
        if not head or not head.next:
            return head
        shadow_head = ListNode(next=head)
        prev = shadow_head

        while head and head.next:
            node_1 = head
            node_2 = head.next

            # Swapping.
            prev.next = node_2
            node_1.next, node_2.next = node_2.next, node_1

            # Reassign pointers, prep for next iteration.
            prev = node_1
            head = node_1.next

        return shadow_head.next
