#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 状态定义：
        # hold  表示当前持有股票时的最大收益
        # sell  表示当天卖出股票时的最大收益
        # reset 表示当天处于冷冻期或休息状态（不持有股票）的最大收益
        hold = -prices[0]  # 第一天买入，收益为 -prices[0]
        sell = 0           # 第一天不能卖出
        reset = 0          # 第一天休息，收益为 0

        # 从第二天开始遍历
        for price in prices[1:]:
            pre_sell = sell  # 记录前一天卖出的收益，用于冷冻期状态转移

            # 持有股票：
            #   1. 之前就已经持有股票
            #   2. 今天从“休息/冷冻期”状态买入
            hold = max(hold, reset - price)

            # 卖出股票：
            #   1. 保持之前卖出的状态
            #   2. 今天从“持有股票”状态卖出
            sell = max(sell, hold + price)

            # 冷冻期/休息状态：
            #   1. 保持之前的休息状态
            #   2. 昨天刚刚卖出股票，进入冷冻期
            reset = max(reset, pre_sell)

        # 最后一天的最大收益在“卖出”或“休息”状态下
        return max(sell, reset)
        
# @lc code=end

