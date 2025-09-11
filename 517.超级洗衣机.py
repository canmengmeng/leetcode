#
# @lc app=leetcode.cn id=517 lang=python3
#
# [517] 超级洗衣机
#

# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        # 如果总衣服数不能整除洗衣机数量，则无法均分，直接返回 -1
        if sum(machines) % len(machines) != 0:
            return -1

        # 每台洗衣机最终应该有的平均衣服数
        avg = sum(machines) // len(machines)
        
        # cur_sum 表示从左到右累积的衣服“流动差值”
        # min_res 表示所需的最大操作次数
        cur_sum = 0
        min_res = 0

        for machine in machines:
            # 当前洗衣机相对于平均值的差额
            diff = machine - avg
            # 累积流动量：表示到当前机器为止，需要从左边流向右边(正数)或右边流向左边(负数)的衣服总量
            cur_sum += diff

            # 更新最少操作次数：
            # 1. machine - avg：当前机器需要单独处理的数量（如果特别多）
            # 2. abs(cur_sum)：前缀流动的最大压力（某个时刻累积需要移动的衣服总量）
            min_res = max(min_res, diff, abs(cur_sum))

        return min_res

        
# @lc code=end

