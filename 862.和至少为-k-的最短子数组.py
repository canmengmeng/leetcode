#
# @lc app=leetcode.cn id=862 lang=python3
#
# [862] 和至少为 K 的最短子数组
#

# @lc code=start
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            
        min_len = n + 1
        
        # 这是一个关键的数据结构，它将存储我们已经遇到的前缀和
        # 我们希望它是有序的，以便快速查找
        # 我们用一个单调栈/队列的变体来维护
        # `dq` 存储的是前缀和数组的下标，并且其对应的前缀和是单调递增的
        dq = []

        for j in range(n + 1):
            # 寻找满足 prefix_sum[i] <= prefix_sum[j] - k 的最大的 i
            # dq 维护的是一个前缀和单调递增的下标序列
            # 因此我们可以用二分查找
            target = prefix_sum[j] - k
            
            low, high = 0, len(dq) - 1
            found_idx = -1
            while low <= high:
                mid = (low + high) // 2
                if prefix_sum[dq[mid]] <= target:
                    found_idx = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            if found_idx != -1:
                i = dq[found_idx]
                min_len = min(min_len, j - i)

            # 维护 dq，使得 prefix_sum[dq[...]] 是单调递增的
            while dq and prefix_sum[dq[-1]] >= prefix_sum[j]:
                dq.pop()
            dq.append(j)

        return min_len if min_len != n + 1 else -1
# @lc code=end

