#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (42.55%)
# Likes:    2457
# Dislikes: 328
# Total Accepted:    428.1K
# Total Submissions: 1M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(m[digits[0]])
        
        prev = self.letterCombinations(digits[:-1])
        additional = m[digits[-1]]
        return [s + c for s in prev for c in additional]

