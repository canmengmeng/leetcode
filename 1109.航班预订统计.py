#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 初始化差分数组，用于高效处理区间加法
        answer = [0] * n

        # 遍历所有预订记录
        for first, last, seats in bookings:
            # 差分法核心：
            # 区间 [first, last] 的每个位置都要 +seats
            # 因此在 first-1 位置加上 seats，
            # 并在 last 位置减去 seats（表示区间结束）
            answer[first - 1] += seats
            if last < n:          # 防止越界（因为航班编号从1到n）
                answer[last] -= seats

        # 通过前缀和恢复实际的预订数
        # 累加差分数组即可得到每个航班的真实座位数
        for i in range(1, n):
            answer[i] += answer[i - 1]

        # 返回每个航班的最终预订结果
        return answer
        
# @lc code=end

