#
# @lc app=leetcode.cn id=2477 lang=python3
#
# [2477] 到达首都的最少油耗
#

# @lc code=start
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        import math
        # 1. 构建邻接表来表示图
        adj = [[] for _ in range(len(roads) + 1)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)

        # 使用一个非局部变量来累积总油耗
        self.total_fuel = 0

        def dfs(u, parent):
            """
            深度优先搜索函数。
            返回以 u 为根的子树中的代表总数。
            在回溯时计算 u 到 parent 这条路的油耗。
            """
            # 初始化：当前节点 u 有1名代表
            representatives = 1
            
            # 遍历 u 的所有邻居
            for v in adj[u]:
                # 如果邻居不是父节点，说明是子节点
                if v != parent:
                    # 递归调用，并累加子树的代表数
                    representatives += dfs(v, u)
            
            # 如果当前节点不是首都，计算到其父节点的油耗
            if u != 0:
                # 从 u 出发的总代表数是 representatives
                # 需要的车辆数是 ceil(representatives / seats)
                cars_needed = math.ceil(representatives / seats)
                # cars_needed = (representatives + seats - 1) // seats # 整数除法实现
                
                # 累加到总油耗中
                self.total_fuel += cars_needed
            
            # 返回当前子树的总代表数
            return representatives

        # 从首都0开始DFS，-1表示没有父节点
        dfs(0, -1)
        
        return self.total_fuel
        
# @lc code=end

