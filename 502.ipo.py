#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        计算在最多完成 k 个项目后可以获得的最大资本。
        """
        import heapq
        n = len(profits)
        
        # 1. 将项目打包成 (capital, profit) 对，并按 capital 排序
        projects = sorted(zip(capital, profits))
        
        # 最大堆，用于存放当前可做项目的利润
        # Python 的 heapq 是最小堆，所以我们存入利润的相反数来模拟最大堆
        affordable_projects_heap = []
        
        project_idx = 0 # 指针，用于遍历排序后的 projects 列表
        
        # 2. 主循环，最多进行 k 次投资
        for _ in range(k):
            # 3. 将所有当前资本 w '解锁' 的项目利润放入最大堆
            while project_idx < n and projects[project_idx][0] <= w:
                # projects[project_idx][0] 是 capital
                # projects[project_idx][1] 是 profit
                profit = projects[project_idx][1]
                heapq.heappush(affordable_projects_heap, -profit) # 存入负数
                project_idx += 1
                
            # 4. 如果没有可做的项目，提前结束
            if not affordable_projects_heap:
                break
                
            # 5. 贪心选择：做利润最高的项目
            max_profit = -heapq.heappop(affordable_projects_heap) # 取出时再变回正数
            w += max_profit
            
        return w
        
# @lc code=end

