#
# @lc app=leetcode.cn id=1947 lang=python3
#
# [1947] 最大兼容性评分和
#

# @lc code=start
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        '''
        示例 1：

        输入：students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
        输出：8
        解释：按下述方式分配学生和导师：
        - 学生 0 分配给导师 2 ，兼容性评分为 3 。
        - 学生 1 分配给导师 0 ，兼容性评分为 2 。
        - 学生 2 分配给导师 1 ，兼容性评分为 3 。
        最大兼容性评分和为 3 + 2 + 3 = 8 。
        '''
        m = len(students)  # 学生和导师的数量
        n = len(students[0]) # 答案的数量

        # 1. 预处理 cost 矩阵
        # cost[i][j] 表示学生 i 和导师 j 的兼容性评分
        cost = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score = 0
                for k in range(n):
                    if students[i][k] == mentors[j][k]:
                        score += 1
                cost[i][j] = score

        # 2. 初始化 DP 数组
        # dp[mask] 表示当导师的分配状态为 mask 时的最大兼容性评分和
        # mask 的第 j 位为 1 表示导师 j 已被分配
        dp = [0] * (1 << m)

        # 3. 状态转移
        # 遍历所有可能的导师分配状态 mask
        for mask in range(1 << m):
            stu_num = bin(mask).count('1') - 1
            for i in range(m):  # 遍历所有老师
                if (mask >> i) & 1 == 1:
                    # 如果在，说明这个状态 mask 可能是通过将 stu_num 分配给导师 i 得到的。
                    # 那么，前一个状态就是 mask 中没有 i 的状态
                    pre_mask = mask ^ (1 << i)
                    dp[mask] = max(dp[mask], dp[pre_mask] + cost[stu_num][i])
        
        # 4. 返回最终结果
        # 最终的 mask 是所有位都为 1，表示所有导师都已被分配
        return dp[(1 << m) - 1]


        
        
# @lc code=end

