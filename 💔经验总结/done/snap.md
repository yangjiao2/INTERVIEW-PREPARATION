```
"""
/**
* give a sorted list [1, 3, 4, 5, 7, 8, 10, 15]
* input is size of the result (N) and minium distance (X) between those numbers
* return is true or false, true means you can find those numbers
*
* sample 1
* N = 3
*
* X = 5 result is true // [1, 7, 15] [1, 8, 15] [1, 10, 15] ... [3, 8, 15]
* X = 6 result is true // [1, 7, 15]

question: return true or false, true if you can find the combination
*/
"""

# ctr = 0 # size
# while (ctr < N):
# start = lst[0]
# for i in range( len(lst)):

    # (start + X) ctr++
    # start = start + X

def sol(lst, N, X):
    if len(lst) == 0:
        return False
    ctr = 1
    prev = lst[0]
    for i in range(len(lst)):

        if (lst[i] - prev) >= X:
            prev = lst[i]
            ctr += 1
        if (N == ctr):
            return True
    return False


# def sol2(lst, N, X):
#     if len(lst) == 0:
#         return False
#     ctr = 1
#     prev = lst[0]
#     res = [lst[0]]
#     for i in range(len(lst)):
#         if (lst[i] - prev) >= X:
#             res.append(lst[i])
#             prev = lst[i]
#             ctr += 1
#         if (N == ctr):

#             return True
#     return False

def sol2(lst, N, X):
    if len(lst) == 0:
        return False
    if (lst[-1] - lst[0] <= (N-1)*X):
        return False

    res = []

    def dfs(start_index, path, res):
        if (len(path) == N):
            res.append(path)

        for i in range(start_index, len(lst)):
            if (len(path) == 0):
                dfs(i+1, path + [lst[i]], res)
            elif (lst[i] - path[-1]) >= X:
                dfs(i, path + [lst[i]], res)

    dfs(0, [], res)
    return res



lst1= [1, 3, 4, 5, 7, 8, 10, 15]
print(sol2(lst1, 3, 5))
print(sol2(lst1, 3, 6))
# print(sol(lst1, 3, 8))

# [1, 3, 4] N = 3, X = 4



    # def binarysearch(): # index of number after return 7's index, ctr ++ , start_index = index





```
