#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        import heapq

        # 统计每个单词的频率
        count = Counter(words)
        # 使用堆来获取前 k 个高频单词
        # 这里我们使用 (-频率, 单词) 作为堆元素，这样可以确保频率高的单词在前，
        # 如果频率相同，字典序较小的单词在前
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        # 提取前 k 个元素
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
        
# @lc code=end

