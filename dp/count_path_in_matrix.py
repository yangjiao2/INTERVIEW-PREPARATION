    def countPaths(self, A):
        m, n, mod = len(A), len(A[0]), 10 ** 9 + 7
        dp = [[1] * n for i in range(m)]
        for a, i, j in sorted([A[i][j], i, j] for i in range(m) for j in range(n)):
            for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
                if 0 <= x < m and 0 <= y < n and A[x][y] < A[i][j]:
                    dp[i][j] += dp[x][y] % mod
        return sum(map(sum, dp)) % mod
