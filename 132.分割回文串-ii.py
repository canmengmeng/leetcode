#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
class Solution:
    def minCut1(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        ans = float('inf')
        for i in range(1, len(s)):
            ans = min(ans, self.minCut1(s[:i]) + self.minCut1(s[i:]) + 1)
        return int(ans)
    
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)] # dp[i]表示s[0...i]的最小分割数 
        for j in range(1, n):
            for i in range(j+1): # 如果s[i...j]是回文串，则dp[j]为s[0...i-1]组成的加一份切割，也就是dp[j] = min(dp[j], dp[i-1]+1)
                if s[i:j+1] == s[i:j+1][::-1]:
                    if i == 0:
                        dp[j] = 0
                    else:
                        dp[j] = min(dp[j], dp[i-1]+1)
        return int(dp[-1])
    
    
