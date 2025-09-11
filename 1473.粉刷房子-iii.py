#
# @lc app=leetcode.cn id=1473 lang=python3
#
# [1473] 粉刷房子 III
#

# @lc code=start
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        """
        LeetCode 1473. 粉刷房子 III
        三维动态规划解决
        houses: 房子的初始颜色，0表示未涂色
        cost: 粉刷成本矩阵
        m: 颜色种类 (1-indexed)
        n: 房子数量
        target: 目标街区数
        """
        
        # dp[i][j][k] 表示粉刷完第 i 个房子，其颜色是 j+1，且目前有 k 个街区的最低成本
        # i: 0 to n-1 (房子索引)
        # j: 0 to m-1 (颜色索引)
        # k: 0 to target (街区数，注意 k 应该从 1 开始计数，所以数组大小是 target+1)
        n, m = m, n
        # 初始化 dp 数组为无穷大
        dp = [[[1e19] * (target + 1) for _ in range(m)] for _ in range(n)]

        # 处理第一个房子 (i = 0)
        for j in range(m): # 遍历所有颜色 j+1
            if houses[0] == 0: # 如果第一个房子未涂色
                dp[0][j][1] = cost[0][j] # 涂 j+1 颜色，1个街区，成本为 cost[0][j]
            elif houses[0] == j + 1: # 如果第一个房子已涂色且颜色是 j+1
                dp[0][j][1] = 0 # 成本为 0
        
        # 从第二个房子开始迭代 (i = 1 to n-1)
        for i in range(1, n):
            for j in range(m): # 当前房子涂颜色 j+1
                if houses[i] != 0 and houses[i] != j + 1: # 如果当前房子已涂色但颜色不对
                    continue # 跳过，因为不能涂这个颜色
                
                # current_paint_cost 是当前房子涂 j+1 颜色的成本 (如果已涂色则为0)
                current_paint_cost = cost[i][j] if houses[i] == 0 else 0
                
                for k_blocks in range(1, target + 1): # 遍历当前可能的街区数
                    for prev_j in range(m): # 遍历前一个房子 prev_dp 的所有可能颜色 prev_j+1
                        if dp[i-1][prev_j][k_blocks] == 1e9: # 如果前一个状态不可达
                            continue
                        
                        if j == prev_j: # 和前一个房子同色，街区数不变
                            dp[i][j][k_blocks] = min(dp[i][j][k_blocks], dp[i-1][prev_j][k_blocks] + current_paint_cost)
                        elif k_blocks > 1: # 和前一个房子不同色，街区数增加1，所以前一个状态是 k_blocks-1
                            dp[i][j][k_blocks] = min(dp[i][j][k_blocks], dp[i-1][prev_j][k_blocks-1] + current_paint_cost)
        
        # 找到所有最终状态中成本最小的
        ans = 1e9
        for j in range(m):
            ans = min(ans, dp[n-1][j][target])
        
        return ans if ans != 1e9 else -1 # 如果为 inf 则表示无法达到目标街区数
        
# @lc code=end

