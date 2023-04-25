'''

##S##
C###C
##C##

output: shortest time to eat all the candies
for the above: ans: 9

'''


def sol(matrix, start_point=(0, 2)):
    # visited candy and time
    m, n = len(matrix), len(matrix[0])
    
    visited = {}
    # queue = [(cur_position, time, candies_eaten)]
    q = [[(start_point), 0, 0]]
    
    # early return
    if m == 0 or n == 0:
        return -1
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    ctr = 0
    # loop through, find all "C"
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == "C":
                ctr += 1
                
    while q:
        cur = q.pop(0)
        x, y = cur[0]
        time = cur[1]
        candies = cur[2]
        
        if candies == ctr:
            return time
        for dx, dy in dirs:
            if (0 <= x + dx < m and 0 <= y + dy < n):
                nx, ny =  x + dx , y + dy
                time += 1
                print (nx, ny, time, candies)
                if (matrix[nx][ny] == "C"):
                    if (nx, ny) in visited:     
                        if visited[(nx, ny)] > time:
                            visited[(nx, ny)] = time
                            q.append([(nx, ny), time, candies + 1])
                        else:
                            continue
                    else:
                        visited[(nx, ny)] = time
                        q.append([(nx, ny), time, candies + 1])
                else:
                    q.append([(nx, ny), time, candies])
                
print (sol([
['#','#','S', '#','#'],
['C','#','#', '#','C'],
['#','#','C', '#','3']
], ))
               
                    
                    
            
    
    
    
    
    
    
class Solution:
    
    
    
    
    def exist(self, b: List[List[str]], w: str) -> bool:
        dirs = [[0,1],[-1,0],[0,-1],[1,0]]
        
        if not b or not b[0]:
            return False
        
        if not w:
            return True
        
        m, n = len(b), len(b[0])
        v = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if self.R(b, w, v, m, n, i, j, 0):
                    return True
        
        return False
    
    def R(self, b: List[List[str]], w: str, v: List[List[bool]], m: int, n: int, i: int, j: int, index: int) -> bool:
        if index == len(w):
            return True
        
        if 0 <= i < m and 0 <= j < n and not v[i][j] and b[i][j] == w[index]:
            v[i][j] = True
            
            for d in dirs:
                if self.R(b, w, v, m, n, i + d[0], j + d[1], index + 1):
                    # v[i][j] = False
                    return True
            
            v[i][j] = False
        
        return False
        
        
'''

##S##
C###C
##C##

output: shortest time to eat all the candies
for the above: ans: 9

'''


def sol(matrix, start_point=(0, 2)):
    # visited candy and time
    m, n = len(matrix), len(matrix[0])
    
    visited = {}
    # queue = [(cur_position, time, candies_eaten)]
    q = [[(start_point), 0, 0]]
    
    # early return
    if m == 0 or n == 0:
        return -1
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    ctr = 0
    # loop through, find all "C"
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == "C":
                ctr += 1
    
    time = 0
    dfs(start_point[0], start_point[1], 0, ctr)
    
    return time
    
    def dfs(inputx, inputy, time, candies):     
    # while q:
    #     cur = q.pop(0)
        # x, y = cur[0]
        # time = cur[1]
        # candies = cur[2]
        
        if ctr == 0:
            return time
        for dx, dy in dirs:
            if (0 <= x + dx < m and 0 <= y + dy < n):
                nx, ny =  x + dx , y + dy
                time += 1
                # print (nx, ny, time, candies)
                
                matrix[inputx][inputy] == ""
                if (matrix[nx][ny] == "C"):
                    if (nx, ny) in visited:     
                        if visited[(nx, ny)] > time:
                            visited[(nx, ny)] = time
                            q.append([(nx, ny), time, candies + 1])
                        else:
                            continue
                    else:
                        visited[(nx, ny)] = time
                        q.append([(nx, ny), time, candies + 1])
                else:
                    q.append([(nx, ny), time, candies])
                
print (sol([
['#','#','S', '#','#'],
['C','#','#', '#','C'],
['#','#','C', '#','3']
], ))
               
                    
                    
            
    
    
    
    
    
    
    
    