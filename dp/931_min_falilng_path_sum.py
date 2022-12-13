# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.


class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * n] * n
        for r in range(1, n):
            for c in range(m):
                

                if c == 0: 
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])
                elif c == m-1:
                    matrix[r][c] += min(matrix[r-1][c-1], matrix[r-1][c]) 
                else:
                    matrix[r][c] += min(matrix[r-1][c-1], matrix[r-1][c], matrix[r-1][c+1])
        print(matrix)
        return min(matrix[n-1])