#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        def compare(x, y):
            """
            比较函数，遵循 cmp(a, b) 规范：
            - 返回 -1 如果 a < b
            - 返回 1 如果 a > b
            - 返回 0 如果 a == b
            """
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
        
# @lc code=end

