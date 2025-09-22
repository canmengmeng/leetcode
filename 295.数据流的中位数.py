#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq
class MedianFinder:
    """
    该类通过维护两个堆来高效地查找数据流的中位数。
    - self.small_half：一个最大堆，存储数据流中较小的一半元素。
    - self.large_half：一个最小堆，存储数据流中较大的一半元素。
    """

    def __init__(self):
        # self.small_half 用于存储较小的一半数字，它是一个最大堆。
        # Python的heapq默认是最小堆，所以我们通过存储负数来模拟最大堆。
        self.small_half = []  # max_heap

        # self.large_half 用于存储较大的一半数字，它是一个最小堆。
        self.large_half = []  # min_heap
        

    def addNum(self, num: int) -> None:
        """
        向数据结构中添加一个新数字，并维护两个堆的平衡。

        时间复杂度: O(log n)，其中n是当前数字的总数。
        堆的插入和弹出操作都是 O(log n)。

        空间复杂度: O(n)，用于存储所有数字。
        """
        heapq.heappush(self.small_half, -num)
        if self.small_half and self.large_half and (-self.small_half[0] > self.large_half[0]):
            heapq.heappush(self.large_half, -heapq.heappop(self.small_half))
        while self.small_half and len(self.small_half) > len(self.large_half) + 1:
            heapq.heappush(self.large_half, -heapq.heappop(self.small_half))
        while self.large_half and len(self.large_half) > len(self.small_half):
            heapq.heappush(self.small_half, -heapq.heappop(self.large_half))
        

    def findMedian(self) -> float:
        """
        返回当前所有元素的中位数。

        时间复杂度: O(1)，因为我们只需要访问两个堆的堆顶元素。
        """
        # 如果元素总数为奇数，中位数在 small_half 的堆顶。
        if len(self.small_half) > len(self.large_half):
            # 因为 small_half 存的是负数，所以需要取反。
            return -self.small_half[0]
        # 如果元素总数为偶数，中位数是两个堆顶元素的平均值。
        else:
            return (-self.small_half[0] + self.large_half[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

