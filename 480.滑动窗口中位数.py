#
# @lc app=leetcode.cn id=480 lang=python3
#
# [480] 滑动窗口中位数
#

# @lc code=start
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        import heapq
        from collections import defaultdict
        """
        使用两个堆（大顶堆 small, 小顶堆 large）来维护滑动窗口的中位数。
        small: 存储较小的一半元素（存相反数，大顶堆效果）
        large: 存储较大的一半元素（小顶堆）
        """
        small, large = [], []
        sizes = {"small": 0, "large": 0}  # 分别记录两个堆的有效元素数量
        invalid = defaultdict(int)         # 延迟删除的无效元素

        # --- 辅助函数 ---
        def prune(heap):
            """移除堆顶的无效元素"""
            while heap and invalid[( -heap[0] if heap is small else heap[0] )] > 0:
                num = -heapq.heappop(heap) if heap is small else heapq.heappop(heap)
                invalid[num] -= 1

        def balance():
            """平衡两个堆，使得 small 的元素数 >= large，且差不超过 1"""
            if sizes["small"] > sizes["large"] + 1:
                prune(small)
                heapq.heappush(large, -heapq.heappop(small))
                sizes["small"] -= 1
                sizes["large"] += 1
            if sizes["large"] > sizes["small"]:
                prune(large)
                heapq.heappush(small, -heapq.heappop(large))
                sizes["small"] += 1
                sizes["large"] -= 1

        def get_median():
            """获取当前窗口的中位数"""
            prune(small)
            prune(large)
            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0

        # --- 初始化前 k 个元素 ---
        for i in range(k):
            heapq.heappush(small, -nums[i])
            sizes["small"] += 1

        # 调整平衡
        while sizes["small"] > sizes["large"] + 1:
            heapq.heappush(large, -heapq.heappop(small))
            sizes["small"] -= 1
            sizes["large"] += 1

        result = [get_median()]

        # --- 滑动窗口 ---
        for i in range(k, len(nums)):
            out_num, in_num = nums[i - k], nums[i]

            # 标记待删除的元素
            invalid[out_num] += 1
            # prune(small)
            if small and out_num <= -small[0]:
                sizes["small"] -= 1
            else:
                sizes["large"] -= 1

            # 插入新元素
            prune(small)
            if small and in_num <= -small[0]:
                heapq.heappush(small, -in_num)
                sizes["small"] += 1
            else:
                heapq.heappush(large, in_num)
                sizes["large"] += 1

            # 调整平衡
            balance()

            # 记录中位数
            result.append(get_median())

        return result
            
# @lc code=end

