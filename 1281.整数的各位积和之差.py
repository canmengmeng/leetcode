#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        sum_ = 0
        mul_ = 1
        for char in s:
            sum_ += int(char)
            mul_ *= int(char)
        return mul_ - sum_
# @lc code=end

