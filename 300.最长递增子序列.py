#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        """
        最长递增子序列的 O(N log N) 解法
        
        时间复杂度: O(N log N) - N次循环，每次循环内有一次 O(log N) 的二分查找
        空间复杂度: O(N) - 最坏情况下，tails 数组会存储所有元素
        """
        if not nums:
            return 0
        
        # tails[i] 表示长度为 i+1 的所有递增子序列中，结尾最小的那个元素
        tails = []
        
        for num in nums:
            # bisect_left 找到 num 在 tails 中应该插入的位置
            # 这个位置 i 也是 tails 中第一个大于等于 num 的元素的位置
            i = bisect.bisect_left(tails, num)
            
            if i == len(tails):
                # 如果 num 大于 tails 中所有元素，直接追加，LIS 长度加 1
                tails.append(num)
            else:
                # 否则，用 num 覆盖掉那个第一个大于等于它的元素
                # 这意味着我们找到了一个结尾更小的、长度为 i+1 的 LIS
                tails[i] = num
                
        return len(tails)
        
# @lc code=end

