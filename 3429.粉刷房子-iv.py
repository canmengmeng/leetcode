#
# @lc app=leetcode.cn id=3429 lang=python3
#
# [3429] 粉刷房子 IV
#

# @lc code=start
class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        """
        解决粉刷房子 IV 问题
        """
        # prev_dp[c1][c2] 存储处理完前一对房子后，
        # 左边房子颜色为 c1，右边房子颜色为 c2 的最低成本
        prev_dp = [[float('inf')] * 3 for _ in range(3)]
        
        num_pairs = n // 2
        
        # --- 基准情况: i = 0 ---
        # 处理最外层的一对房子 (0, n-1)
        for c1 in range(3):
            for c2 in range(3):
                # 对称约束
                if c1 != c2:
                    prev_dp[c1][c2] = cost[0][c1] + cost[n - 1][c2]

        # --- 动态规划: i 从 1 到 num_pairs - 1 ---
        # 从第二对房子 (1, n-2) 开始向内迭代
        for i in range(1, num_pairs):
            curr_dp = [[float('inf')] * 3 for _ in range(3)]
            
            for c1 in range(3):  # 当前左边房子 i 的颜色
                for c2 in range(3):  # 当前右边房子 n-1-i 的颜色
                    
                    # 对称约束
                    if c1 == c2:
                        continue
                    
                    # 寻找满足约束的最小的前一步成本
                    min_prev_cost = float('inf')
                    for pc1 in range(3):  # 前一个左边房子 i-1 的颜色
                        for pc2 in range(3):  # 前一个右边房子 n-i 的颜色
                            # 相邻约束
                            if c1 != pc1 and c2 != pc2:
                                min_prev_cost = min(min_prev_cost, prev_dp[pc1][pc2])
                    
                    # 如果存在有效的前一步
                    if min_prev_cost != float('inf'):
                        current_pair_cost = cost[i][c1] + cost[n - 1 - i][c2]
                        curr_dp[c1][c2] = current_pair_cost + min_prev_cost
            
            # 更新 dp 表，为下一轮迭代做准备
            prev_dp = curr_dp

        # --- 最终结果 ---
        # 从最后的状态中找到全局最小值
        min_total_cost = float('inf')
        for row in prev_dp:
            min_total_cost = min(min_total_cost, min(row))
            
        return min_total_cost if min_total_cost != float('inf') else -1
# @lc code=end

