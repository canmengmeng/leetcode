#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)] # (value, original_index)
        result = [0] * n

        def merge_sort(enum):
            mid = len(enum) // 2
            if mid == 0:
                return enum
            
            left = merge_sort(enum[:mid])
            right = merge_sort(enum[mid:])
            
            # 合并并计算
            enum = merge(left, right)
            return enum
        
        def merge(left, right):
            merged = []
            i, j = 0, 0
            
            while i < len(left) and j < len(right):
                # 如果左边元素小于等于右边元素,说明right前j个比left[i]小
                if left[i][0] <= right[j][0]:
                    # 此时，右边数组中已经有 j 个元素被合并（即比 left[i] 小）
                    # 这些元素在原数组中都位于 left[i] 的右侧
                    result[left[i][1]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    # 右边元素更小，先合并右边元素
                    merged.append(right[j])
                    j += 1
            
            # 处理剩余的左边数组元素，此时剩余的左边全部都比右边元素大
            while i < len(left):
                result[left[i][1]] += j # 此时右边数组已全部合并
                merged.append(left[i])
                i += 1
                
            # 处理剩余的右边数组元素
            while j < len(right):
                merged.append(right[j])
                j += 1
                
            return merged

        merge_sort(arr)
        return result
        
# @lc code=end

