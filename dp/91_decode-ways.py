class Solution:
    def numDecodings(self, s: str) -> int:
        # situation:
        # 1 digit: dp[i] = 0 if i == '0' else dp[i-1]
        # 2 digit: dp[i] += dp[i+2] if valid else dp[i-1]

        dp = [0 for x in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1   # first char

        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]




# class Solution:
#     def numDecodings(self, s: str) -> int:

#         @lru_cache(None)
#         def dfs(s):
#             if not s: return 1
#             if s[0]=='0': return 0

#             if len(s) > 1 and int(s[:2]) < 27:
#                 return dfs(s[1:]) + dfs(s[2:])
#             return dfs(s[1:])

#         return dfs(s)
