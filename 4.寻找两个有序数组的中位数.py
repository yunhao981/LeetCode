#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.46%)
# Likes:    1955
# Dislikes: 0
# Total Accepted:    127.3K
# Total Submissions: 349.3K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l//2)
        else:
            return (self.kth(nums1, nums2, l//2-1) + self.kth(nums1, nums2, l//2))/2

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]

        ia, ib = len(a)//2, len(b)//2
        ma, mb = a[ia], b[ib]

        if k > ia + ib:
            if ma > mb:
                return self.kth(a, b[ib+1:], k-ib-1)

            else:
                return self.kth(b, a[ia+1:], k-ia-1)
        
        else:
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

# @lc code=end

