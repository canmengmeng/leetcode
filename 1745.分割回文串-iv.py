#
# @lc app=leetcode.cn id=1745 lang=python3
#
# [1745] 分割回文串 IV
#

# @lc code=start
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        
        n = len(s)
        dp = [[False] * n for _ in range(n)] # dp[i][j]表示s[i...j]是否是回文串
        # 初始化dp，dp[i][i] = True，dp[i][i+1] = s[i] == s[i+1]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            dp[i][i+1] = s[i] == s[i+1]
        # 题意就是找一个i, j，满足dp[0][i] and dp[i+1][j] and dp[j+1][n-1] 为 True
        # 状态转移方程：dp[i][j] = dp[i+1][j-1] and s[i] == s[j] if j - i >= 2
        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        for i in range(n-2):
            for j in range(i+1, n-1):
                if dp[0][i] and dp[i+1][j] and dp[j+1][n-1]:
                    return True
        return False
# @lc code=end

