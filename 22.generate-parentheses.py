#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (56.38%)
# Likes:    3124
# Dislikes: 192
# Total Accepted:    376.3K
# Total Submissions: 666.6K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution:
    def generateParenthesis(self, n: int, open=0) -> List[str]:
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
                [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)
        

