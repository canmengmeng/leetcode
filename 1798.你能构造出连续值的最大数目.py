#
# @lc app=leetcode.cn id=1798 lang=python3
#
# [1798] 你能构造出连续值的最大数目
#

# @lc code=start
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # 1. 排序
        coins.sort()
        
        # 2. 初始化可达范围
        reachable_sum = 0
        
        # 3. 遍历数组
        for num in coins:
            if num <= reachable_sum + 1:
                reachable_sum += num
            else:
                # 出现断层
                return reachable_sum + 1
                
        # 4. 如果循环结束
        return reachable_sum + 1
        
# @lc code=end

