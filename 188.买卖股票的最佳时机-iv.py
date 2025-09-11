#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp[i][j]:
        # i 表示第几次交易（0 到 k-1）
        # j 表示状态（0：持有股票，1：卖出股票后的现金）
        dp = [[0] * 2 for _ in range(k)]
        
        # 初始化：假设在第一天进行第 i 次买入（价格为 prices[0]）
        # 持有股票的代价是 -prices[0]，无论第几次买入都从 -prices[0] 开始
        for i in range(k):
            dp[i][0] = -prices[0]
        
        # 遍历每天的股价
        for price in prices:
            for i in range(k):
                # 第 i 次买入：
                #   - 如果 i == 0，只能直接买入，dp[0][0] = max(dp[0][0], -price)
                #   - 如果 i > 0，可以从上一次交易（i-1 次卖出）的现金中买入
                dp[i][0] = max(dp[i][0], dp[i-1][1] - price if i > 0 else -price)
                
                # 第 i 次卖出：
                #   卖出后等于持有股票的价值 + 当前价格
                dp[i][1] = max(dp[i][1], dp[i][0] + price)
        
        # 最多进行 k 次交易，返回第 k 次卖出的最大收益
        return dp[-1][1]
# @lc code=end

