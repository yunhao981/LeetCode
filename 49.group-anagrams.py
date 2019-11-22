#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (48.52%)
# Likes:    2226
# Dislikes: 138
# Total Accepted:    436.9K
# Total Submissions: 859.9K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for w in sorted(strs):
            key = tuple(sorted(w))
            ans[key] = ans.get(key, []) + [w]
        return ans.values()
        
# @lc code=end

