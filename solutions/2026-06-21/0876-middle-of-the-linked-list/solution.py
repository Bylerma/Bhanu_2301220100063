# Number: 0876
# Title: Middle of the Linked List
# Difficulty: Easy
# Tags: Linked List, Two Pointers
# Language: Python3
# URL: https://leetcode.com/problems/middle-of-the-linked-list/
# Date: 2026-06-21
# Runtime: 171ms (Beats 95.40%)
# Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        slow = head
        fast = head
        while fast:
            if fast.next == None:
                return slow
            slow = slow.next
            fast = fast.next.next
        return slow
