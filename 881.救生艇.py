#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 先对体重进行排序（方便贪心匹配最轻和最重的人）
        people = sorted(people)

        left, right = 0, len(people) - 1  # 双指针：left 指向最轻的人，right 指向最重的人
        min_res = 0  # 统计所需的最少船数

        while left <= right:
            # 如果最重的人和最轻的人能同船，就一起上船
            if people[right] + people[left] <= limit:
                left += 1  # 最轻的人也上船
            # 不管能不能同船，最重的人必须走（占一条船）
            right -= 1
            min_res += 1  # 使用一条船

        return min_res
        
# @lc code=end

