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





class Solution(object):
    def findUnsortedSubarray(self, nums):
        if len(nums) <2:
            return 0

        prev = nums[0]
        end = 0
		# find the largest index not in place
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        start = len(nums) - 1
        prev = nums[start]
		# find the smallest index not in place
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        if end != 0:
            return end - start + 1
        else:
            return 0
