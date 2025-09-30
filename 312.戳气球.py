#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 1. 预处理，添加边界 1
        n = len(nums)
        points = [1] + nums + [1]
        
        # 2. 初始化 DP 数组
        # dp[i][j] 表示戳破 (i, j) 区间内所有气球的最大收益
        # 数组大小为 (n+2) x (n+2)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # 3. 状态转移
        for i in range(n + 1, -1, -1):
            for j in range(i + 1, n + 2):
                # k 是在 (i, j) 区间内最后一个被戳破的气球
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + points[i] * points[k] * points[j] + dp[k][j])
        
        # 4. 返回结果
        # 最终结果是戳破 (0, n+1) 区间内所有气球的收益
        return dp[0][n + 1]
        

        
# @lc code=end

