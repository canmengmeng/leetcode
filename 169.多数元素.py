#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt_ = 0
        res_ = None
        for num in nums:
            if cnt_ == 0:
                res_ = num
            cnt_ += (1 if res_ == num else -1)
        return res_
# @lc code=end

