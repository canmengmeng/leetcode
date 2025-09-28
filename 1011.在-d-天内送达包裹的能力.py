#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            """
            检查给定的运力 (capacity) 是否能在指定的天数 (days) 内运完所有包裹。
            """
            # 需要的天数，至少需要1天
            days_needed = 1
            # 当前船上已装载的包裹重量
            current_weight = 0

            # 遍历所有包裹，模拟装载过程
            for w in weights:
                # 如果当前包裹加上已装载的重量超过了船的运力
                if current_weight + w > capacity:
                    # 那么需要新的一天来运输
                    days_needed += 1
                    # 新的这一天，船上的初始重量就是当前这个包裹的重量
                    current_weight = w
                else:
                    # 否则，继续在当天装载这个包裹
                    current_weight += w
            
            # 最终，判断模拟所需的天数是否在允许的天数范围内
            return days_needed <= days
        
        # 1. 确定答案的取值范围 [left, right]
        # 船的最低运力至少要能装下最重的单个包裹
        left = max(weights)
        # 船的最高运力可以是所有包裹的总重量，这样一天就能运完
        right = sum(weights)
        ans = right  # 初始化一个潜在答案为最大值
        # 3. 编写二分查找循环
        while left <= right:
            # mid 是我们当前“猜测”的船的运力
            mid = left + (right - left) // 2

            # 2. 使用 check 函数验证 mid 是否可行
            if check(mid):
                # 如果 mid 这个运力是可行的
                # 记录下这个可行的答案，并尝试寻找更小的运力
                ans = mid
                right = mid - 1
            else:
                # 如果 mid 这个运力不可行，说明船的承载能力太小了
                # 需要增加运力，所以搜索范围变为右半部分
                left = mid + 1
        
        return ans
        
# @lc code=end

