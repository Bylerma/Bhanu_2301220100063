# Number: 0102
# Title: Binary Tree Level Order Traversal
# Difficulty: Medium
# Tags: Tree, Breadth-First Search, Binary Tree
# Language: Python3
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Date: 2026-06-22
# Runtime: 0ms (Beats 100%)
# Memory: 0.00MB (Beats 100%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
        
        q = collections.deque()
        q.append(root)
    
        while q:
            same_level = []

            for _ in range(len(q)):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(same_level)
        
        return res