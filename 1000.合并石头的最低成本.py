#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#

# @lc code=start
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)

        # 关键约束：每次合并减少 k-1 堆，n 堆变 1 堆，共减少 n-1 堆
        # 所以 n-1 必须是 k-1 的倍数
        if k > 2 and n % (k - 1) != 1:
            return -1

        # 1. 预处理前缀和，方便快速计算区间和 sum(i, j)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]

        def get_sum(i, j):
            return prefix_sum[j + 1] - prefix_sum[i]

        # 2. 初始化 DP 数组
        # dp[i][j][m] 表示将 stones[i..j] 合并成 m 堆的最小代价
        # 我们用一个很大的数表示无穷大
        infinity = float('inf')
        dp = [[[infinity] * (k+1) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][1] = 0

        # 4. 状态转移，按区间长度 len 从小到大遍历
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 情况 B: 计算 dp[i][j][m] for m from 2 to k
                # 将 [i,j] 分成 [i,split] 和 [split+1,j]
                # [i,split] 合并成 m-1 堆, [split+1,j] 合并成 1 堆
                for m in range(2, k + 1):
                    for mid in range(i, j):
                        dp[i][j][m] = min(dp[i][j][m], dp[i][mid][m - 1] + dp[mid + 1][j][1])
                
                # 情况 A: 计算 dp[i][j][1]
                # 上一个状态是 [i,j] 已经被合并成了 k 堆
                if dp[i][j][k] < float('inf'):
                    # 注意：只有长度满足 (len-1)%(k-1)==0 的区间才可能合并成1堆
                    # 我们前面的总判断保证了最终结果的可行性，子问题也隐含了这个约束
                    dp[i][j][1] = dp[i][j][k] + get_sum(i, j)
        
        # 5. 返回最终结果
        result = dp[0][n - 1][1]
        return int(result)
        
# @lc code=end

