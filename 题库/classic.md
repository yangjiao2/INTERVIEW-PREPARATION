class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 特判
        size = len(s)
        if size < 2:
            return size
        # key 为字符，val 记录了当前读到的字符的索引，在每轮循环的最后更新
        d = dict()
        left = 0
        # 非空的时候，结果至少是 1 ，因此初值可以设置成为 1
        res = 1
        for right in range(size):

            # d[s[right]] >= left，表示重复出现在滑动窗口内
            # d[s[right]] < left 表示重复出现在滑动窗口之外，之前肯定计算过了
            if s[right] in d and d[s[right]] >= left:
                # 下一个不重复的子串至少在之前重复的那个位置之后
                # 【特别注意】快在这个地方，左边界直接跳到之前重复的那个位置之后
                left = d[s[right]] + 1

            # 此时滑动窗口内一定没有重复元素
            res = max(res, right - left + 1)
            # 无论如何都更新位置
            d[s[right]] = right
        return res




class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        
        cols = len(matrix[0])
        if cols == 0:
            return 0
        
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    res = max(res, dp[i + 1][j + 1])
        
        return res * res


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)