#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.98%)
# Likes:    1604
# Dislikes: 0
# Total Accepted:    161.5K
# Total Submissions: 576.5K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            tmp = self.f(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            
            tmp = self.f(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def f(self, s, l, r):
        while l>=0 and r < len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
# @lc code=end

