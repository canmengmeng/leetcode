#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        动态规划解法
        """
        # dp[i] 表示凑成金额 i 所需的最少货币数
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # 遍历 1 到 amount 的所有金额
        for i in range(1, amount + 1):
            # 对于每个金额，遍历所有货币面值
            for coin in coins:
                if i >= coin:
                    # 状态转移
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        final_result = dp[amount]
        return final_result if final_result != float('inf') else -1
        
# @lc code=end

