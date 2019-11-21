#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (41.64%)
# Likes:    1372
# Dislikes: 47
# Total Accepted:    289.2K
# Total Submissions: 671.5K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = [[]]
        for n in nums:
            newAns = []
            l = len(ans[-1])
            for seq in ans:
                for i in range(l,-1,-1):
                    if i < l and seq[i] == n:
                        break
                    newAns.append(seq[:i] + [n] + seq[i:])
            ans = newAns
        return ans
            
# @lc code=end

