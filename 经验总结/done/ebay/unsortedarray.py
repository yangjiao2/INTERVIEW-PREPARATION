# import requests
# import mysql.connector
# import pandas as pd

# Input: array of numbers (integer)
# Find subarray of the array such that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
# Output: return the shortest subarray of the array
# [2,6,4,8,10,9,15]

# output: [endpoint, endpoint2]


# [2,6,4,8,1,10,9,15]

# 1, 2, 4, 6, 8, 9, 10, 15

# [2, 1, 4]


# smallest: 1, (index), array.index(1)


def sol(array = [2,6,4,8,10,9,3]):
    stack = []
    index = 0
    mapping = {}
    res = [len(array), 0]
    while index != len(array):
        num = array[index]
        if len(stack) == 0:
            stack.append(num)
        elif stack and num > stack[-1]:
            stack.append(num)
        else:
            counter = 0
            while stack and num < stack[-1]:
                last = stack.pop()
                if last in mapping:
                    counter += mapping[last]
                else:
                    counter += 1
            if res[-1] < index:
                res[-1] = index
            if res[0] > counter:
                res[0] = index - counter
            # mapping[num] = index

        index += 1

    print (mapping)

    return res

print (sol()) #[2,6,4,8,10,9,3] => [1, 6]





def findUnsortedSubarray(nums) -> int:
    if nums is None:
        return 0
    if len(nums) == 0 or len(nums) == 1:
        return 0

    max_num = float('-inf')
    end = -2
    # iterate from beginning of array
    # find the last element which is smaller than the last seen max from
    # its left side and mark it as end
    for i in range(len(nums)):
        max_num = max(max_num, nums[i])
        if nums[i] < max_num:
            end = i

    min_num = float('inf')
    begin = -1
    # iterate from end of array
    # find the last element which is bigger than the last seen min from
    # its right side and mark it as begin
    for i in range(len(nums) - 1, -1, -1):
        min_num = min(min_num, nums[i])
        if nums[i] > min_num:
            begin = i

    return [begin, end]
