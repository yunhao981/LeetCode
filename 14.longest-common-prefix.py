#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.98%)
# Likes:    1531
# Dislikes: 1418
# Total Accepted:    518.5K
# Total Submissions: 1.5M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        s = zip(*strs)
        for c in s:
            if(len(set(c))) > 1: break
            ans += c[0]
        return ans


