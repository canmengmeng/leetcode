#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 状态定义：
        # hold  表示当前持有股票时的最大收益
        # sell  表示当天卖出股票时的最大收益
        hold = -prices[0] - fee  # 第一天买入，收益为 -prices[0]
        sell = 0           # 第一天不能卖出

        # 从第二天开始遍历
        for price in prices[1:]:
            # 持有股票：
            #   1. 之前就已经持有股票
            #   2. 今天从“休息/冷冻期”状态买入
            hold = max(hold, sell - price - fee)

            # 卖出股票：
            #   1. 保持之前卖出的状态
            #   2. 今天从“持有股票”状态卖出
            sell = max(sell, hold + price)


        # 最后一天的最大收益在“卖出”或“休息”状态下
        return sell
        
# @lc code=end

