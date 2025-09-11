#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        使用归并排序的思想计算数组中的逆序对数量。
        """
        
        def merge_sort_and_count(sub_arr):
            n = len(sub_arr)
            if n <= 1:
                return sub_arr, 0

            # 分治
            mid = n // 2
            left_half, left_count = merge_sort_and_count(sub_arr[:mid])
            right_half, right_count = merge_sort_and_count(sub_arr[mid:])
            
            # 合并并计算跨区逆序对
            cross_count = 0
            i, j = 0, 0
            len_left, len_right = len(left_half), len(right_half)
            while i < len_left and j < len_right:
                if left_half[i] <= 2 * right_half[j]:
                    i += 1
                else: # left[i] > right[j]
                    # 发现了逆序对
                    cross_count += (len_left - i)
                    # left[i] 以及它之后的所有元素都比 right[j] 大
                    j += 1
            
            # 合并两个有序数组
            merged_arr = merge_and_count(left_half, right_half)
            
            total_count = left_count + right_count + cross_count
            return merged_arr, total_count

        def merge_and_count(left, right):
            merged = []
            i, j = 0, 0
            len_left, len_right = len(left), len(right)

            while i < len_left and j < len_right:
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else: # left[i] > right[j]
                    merged.append(right[j])
                    j += 1
            
            # 将剩余的元素加入
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged

        # 初始调用
        if not nums:
            return 0
        _, total_inversions = merge_sort_and_count(nums)
        return total_inversions
        
# @lc code=end

