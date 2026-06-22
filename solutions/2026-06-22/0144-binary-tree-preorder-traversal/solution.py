# Number: 0144
# Title: Binary Tree Preorder Traversal
# Difficulty: Easy
# Tags: Stack, Tree, Depth-First Search, Binary Tree
# Language: Python3
# URL: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Date: 2026-06-22
# Runtime: 0 ms (Beats 100%)
# Memory: 0.00MB (Beats 100%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs_preorder(node, res):
            if not node:
                return None
            res.append(node.val)
            dfs_preorder(node.left, res)
            dfs_preorder(node.right, res)
        dfs_preorder(root, res)
        return res
