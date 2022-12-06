# Time:  O(m * n)
# Space: O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction_lst = [(0,1), (1, 0) , (0, -1), (-1, 0)]
        direction_index = 0
        n = len(matrix[0])
        res = [-1 for _ in range(n*n)]
        
        direction_coordinates = direction_lst[direction_index]
        coordinates = (0, 0)
        
        for i in range (0, n * n):
            res[i] = matrix[coordinates[0]][coordinates[1]]
            new_coordinates = (coordinates[0] + direction_coordinates[0], coordinates[1] + direction_coordinates[1] )
            new_index = new_coordinates[0]*n + new_coordinates[1]
            if ((new_coordinates[0] < n) and (new_coordinates[1] < n) and (new_coordinates[0] >= 0) and (new_coordinates[1] >= 0) and (res[new_index] == -1)):
                coordinates = new_coordinates
                
            else:
                direction_index = (direction_index + 1) % 4
                direction_coordinates = direction_lst[direction_index]
                coordinates = (coordinates[0] + direction_coordinates[0], coordinates[1] + direction_coordinates[1])
        return res
    
    
    
    
class Solution2(object):
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == []:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            for j in xrange(left, right + 1):
                result.append(matrix[top][j])
            for i in xrange(top + 1, bottom):
                result.append(matrix[i][right])
            for j in reversed(xrange(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(xrange(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result