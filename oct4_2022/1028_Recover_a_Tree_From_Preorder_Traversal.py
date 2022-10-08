# Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        Time: O(n) n is the number of characters in traversal string.
        Space: O(m) m is the number of nodes in the tree.
        """
        dash = "-"
        tree_levels = {}
        depth, node_value, char_idx = 0, 0, 0
        while char_idx < len(traversal):
            if traversal[char_idx] == dash:
                depth += 1
                char_idx += 1
            else:
                while char_idx < len(traversal) and traversal[char_idx].isdigit():
                    node_value = node_value * 10 + int(traversal[char_idx])
                    char_idx += 1

                node = TreeNode(val=node_value)

                if depth != 0:
                    last_node = tree_levels[depth - 1][-1]
                    if not last_node.left:
                        last_node.left = node
                    else:
                        last_node.right = node

                tree_levels[depth] = tree_levels.get(depth, []) + [node]

                # Reset buffer
                depth = 0
                node_value = 0

        return tree_levels[0][0]
