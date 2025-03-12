#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 判断s是否能够被exp匹配
        # 1. 如果exp是空字符串，s也是空字符串才能匹配
        # 2. 如果exp不是空字符串，则需要判断s是否能够被exp匹配
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        # 处理模式串开头是*的情况
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]  # 匹配0次
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] = dp[i][j] or dp[i-1][j]  # 匹配1次或多次
        return dp[m][n]

        
# @lc code=end

