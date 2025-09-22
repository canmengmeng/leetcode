#
# @lc app=leetcode.cn id=795 lang=python3
#
# [795] 区间子数组个数
#

# @lc code=start
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        last1 = -1  # 记录上一个 >= left 的位置
        last2 = -1  # 记录上一个 > right 的位置
        for i, num in enumerate(nums):
            # 更新 last1 和 last2
            if num >= left:
                last1 = i
            if num > right:
                last1 = -1 
                last2 = i
            # 只有当 last1 有效时，才有贡献
            if last1 != -1:
                ans += (last1 - last2)
        return ans
        
# @lc code=end

