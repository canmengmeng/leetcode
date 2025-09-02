#
# @lc app=leetcode.cn id=1353 lang=python3
#
# [1353] 最多可以参加的会议数目
#

# @lc code=start
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[0])
        min_heap = [] 
        res_count = 0
        event_idx = 0
        max_day = -1
        for _, end in events:
            max_day = max(max_day, end)
        for day_idx in range(1, max_day + 1):
            # a. 清理堆中已经过期的会议（结束日期小于当前日期的）
            while min_heap and min_heap[0] < day_idx:
                heapq.heappop(min_heap)
                
            # b. 将今天开始的所有会议的结束日期加入堆中
            while event_idx < len(events) and events[event_idx][0] == day_idx:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1
                
            # c. 如果今天有可参加的会议，就参加一个（结束日期最早的）
            if min_heap:
                heapq.heappop(min_heap)
                res_count += 1
        return res_count

# @lc code=end

