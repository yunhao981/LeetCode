#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (46.02%)
# Likes:    3711
# Dislikes: 463
# Total Accepted:    421.2K
# Total Submissions: 915.3K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# 
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res,  h * (r - l)), l + (height[l] == h), r - (height[r] == h)
        return res
