#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (34.00%)
# Likes:    2202
# Dislikes: 103
# Total Accepted:    377.5K
# Total Submissions: 1.1M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def BinarySearchLeft(A,x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]: 
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def BinarySearchRight(A,x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        left, right = BinarySearchLeft(nums, target), BinarySearchRight(nums, target)
        if left <= right:
            return (left, right)
        else:
            return [-1,-1]
# @lc code=end

