#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][j]:
        # i 表示交易次数（0：第一次买卖，1：第二次买卖）
        # j 表示状态（0：持有股票，1：卖掉股票后的现金）
        dp = [[0] * 2 for _ in range(2)]
        
        # 初始化：
        # 第一次买入：dp[0][0] = -prices[0]
        # 第二次买入：dp[1][0] = -prices[0]（等效为在第一次卖出后再买入）
        dp[0][0] = dp[1][0] = -prices[0]
        
        # 遍历每一天的股价
        for price in prices:
            # 第一次买入：取之前的值和今天买入的最大值
            dp[0][0] = max(dp[0][0], -price)
            # 第一次卖出：取之前的值和今天卖出的最大值
            dp[0][1] = max(dp[0][1], dp[0][0] + price)
            # 第二次买入：取之前的值和在第一次卖出后再买入的最大值
            dp[1][0] = max(dp[1][0], dp[0][1] - price)
            # 第二次卖出：取之前的值和今天卖出的最大值
            dp[1][1] = max(dp[1][1], dp[1][0] + price)
        
        # 最多进行两次交易，所以返回第二次卖出的收益
        return dp[1][1]
        
# @lc code=end

