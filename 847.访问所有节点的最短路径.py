#
# @lc app=leetcode.cn id=847 lang=python3
#
# [847] 访问所有节点的最短路径
#

# @lc code=start
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        import collections
        n = len(graph)
        
        # 如果只有一个节点，路径长度为0
        if n == 1:
            return 0

        # 1. 初始化目标 mask，即所有位都为 1
        final_mask = (1 << n) - 1
        
        # 队列存储状态元组 (u, mask)，u是当前节点，mask是访问过的节点集合
        queue = collections.deque()
        
        # dist[mask][u] 记录到达状态 (u, mask) 的最短路径，同时起到 visited 的作用
        # 初始化为无穷大
        dist = [[float('inf')] * n for _ in range(1 << n)]

        # 我们可以从任何节点开始，所以将所有起始状态加入队列
        for i in range(n):
            # 初始 mask 只包含起始节点 i
            initial_mask = 1 << i
            # (当前节点, 访问集合)
            queue.append((i, initial_mask))
            # 初始距离为 0
            dist[initial_mask][i] = 0

        # 2. BFS 循环
        while queue:
            u, mask = queue.popleft()
            d = dist[mask][u]

            # 3. 探索邻居
            for v in graph[u]:
                # 计算下一个状态的 mask
                new_mask = mask | (1 << v)
                
                # 如果我们找到了一个更短的路径到达状态 (v, new_mask)
                if d + 1 < dist[new_mask][v]:
                    dist[new_mask][v] = d + 1
                    
                    # 检查新状态是否是最终状态
                    if new_mask == final_mask:
                        return d + 1
                        
                    queue.append((v, new_mask))
        
        # 理论上，因为图是连通的（或多个连通分量，但题目保证能访问所有点），
        # 总能找到解，所以这里不会执行到。
        return -1
        
        
# @lc code=end

