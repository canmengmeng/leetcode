#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的数组，以优化二分查找的范围
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        
        # 在较短的数组 nums1 上进行二分查找
        low = 0
        high = m
        
        while low <= high:
            # partitionX 是 nums1 中右边部分的第一个元素的索引
            partitionX = (low + high) // 2
            # partitionY 是根据 partitionX 计算得出的
            # (m + n + 1) // 2 这个技巧可以同时处理奇数和偶数总长度
            partitionY = (m + n + 1) // 2 - partitionX
            
            # 获取分割线左边的最大值
            # 如果 partitionX 是 0，说明 nums1 的左半部分为空
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            # 如果 partitionY 是 0，说明 nums2 的左半部分为空
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            
            # 获取分割线右边的最小值
            # 如果 partitionX 是 m，说明 nums1 的右半部分为空
            minX = float('inf') if partitionX == m else nums1[partitionX]
            # 如果 partitionY 是 n，说明 nums2 的右半部分为空
            minY = float('inf') if partitionY == n else nums2[partitionY]
            
            # 检查是否找到了完美的分割点
            if maxX <= minY and maxY <= minX:
                # 找到了，现在根据总长度的奇偶性计算中位数
                if (m + n) % 2 == 0:
                    # 偶数情况：中位数是左半部分最大值和右半部分最小值的平均
                    left_max = max(maxX, maxY)
                    right_min = min(minX, minY)
                    return (left_max + right_min) / 2.0
                else:
                    # 奇数情况：中位数就是左半部分的最大值
                    return float(max(maxX, maxY))
            elif maxX > minY:
                # partitionX 太大了，需要向左移动
                high = partitionX - 1
            else: # maxY > minX
                # partitionX 太小了，需要向右移动
                low = partitionX + 1
        
        return 0.0
        
# @lc code=end

