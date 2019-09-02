#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (45.84%)
# Likes:    1350
# Dislikes: 120
# Total Accepted:    348.9K
# Total Submissions: 757K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = self
        p.next = head
        while p.next and p.next.next:
            a = p.next
            b = a.next
            p.next, b.next, a.next = b, a, b.next
            p = a
        return self.next



