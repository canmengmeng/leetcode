#
# @lc app=leetcode.cn id=1411 lang=python3
#
# [1411] 给 N x 3 网格图涂色的方案数
#

# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        使用动态规划解决 N x 3 网格图涂色问题。

        核心思想：
        1. 将每一行的涂色模式分为两类：
           - 两色模式 (ABA型): 如 红-黄-红。
           - 三色模式 (ABC型): 如 红-黄-绿。

        2. 定义状态：
           - two_color_count: 涂到当前行，且当前行为“两色模式”的方案数。
           - three_color_count: 涂到当前行，且当前行为“三色模式”的方案数。

        3. 状态转移：
           我们推导从第 i-1 行到第 i 行，两种模式之间如何转换。
           - 假设上一行是“两色模式”(ABA)，下一行可以是：
             - 3种“两色模式” (如 BCB, BAB, CAC)
             - 2种“三色模式” (如 BAC, CAB)
           - 假设上一行是“三色模式”(ABC)，下一行可以是：
             - 2种“两色模式” (如 BAB, BCB)
             - 2种“三色模式” (如 BCA, CAB)

        4. 状态转移方程：
           new_two = prev_two * 3 + prev_three * 2
           new_three = prev_two * 2 + prev_three * 2

        5. 初始状态 (n=1):
           - 两色模式有 3*2 = 6 种。
           - 三色模式有 3*2*1 = 6 种。
        """
        
        # 处理 n=0 的边界情况
        if n == 0:
            return 0

        # 定义模数
        MOD = 10**9 + 7

        # 初始化 n=1 的情况
        # two_color_count: ABA 型方案数
        # three_color_count: ABC 型方案数
        two_color_count = 6
        three_color_count = 6

        # 从 n=2 开始迭代到 n
        # 循环 n-1 次
        for _ in range(n - 1):
            # 临时变量存储上一行的结果
            prev_two_color_count = two_color_count
            prev_three_color_count = three_color_count

            # 根据状态转移方程计算当前行的方案数
            # 当前行是两色模式的方案数
            two_color_count = (prev_two_color_count * 3 + prev_three_color_count * 2) % MOD
            
            # 当前行是三色模式的方案数
            three_color_count = (prev_two_color_count * 2 + prev_three_color_count * 2) % MOD

        # 最终结果是两种模式方案数之和
        total_ways = (two_color_count + three_color_count) % MOD
        
        return total_ways

        
# @lc code=end

