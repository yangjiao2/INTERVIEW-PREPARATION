# Time:  O(m * n)
# Space: O(1)

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction_lst = [(0,1), (1, 0) , (0, -1), (-1, 0)]
        direction_index = 0
        # res = [[-1,-1,-1]] * n wrong cause this is a reference copy
        res = [[-1] * n for _ in range(n)]
        direction_coordinates = direction_lst[direction_index]
        coordinates = (0, 0)
        
        for i in range (1, n * n + 1):
            res[coordinates[0]][coordinates[1]] = i
            
            new_coordinates = (coordinates[0] + direction_coordinates[0], coordinates[1] + direction_coordinates[1] )
            if ((new_coordinates[0] < n) and (new_coordinates[1] < n) and (new_coordinates[0] >= 0) and (new_coordinates[1] >= 0) and (res[new_coordinates[0]][new_coordinates[1]] == -1)):
                coordinates = new_coordinates
                
            else:
                direction_index = (direction_index + 1) % 4
                direction_coordinates = direction_lst[direction_index]
                coordinates = (coordinates[0] + direction_coordinates[0], coordinates[1] + direction_coordinates[1])
        return res
            