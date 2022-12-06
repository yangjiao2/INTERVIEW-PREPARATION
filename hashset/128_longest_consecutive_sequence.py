Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


def longestConsecutive(self, nums):
	s, longest = set(nums), 0
	for num in s:
		if num - 1 in s: continue
		j = 1
		while num + j in s: j += 1
		longest = max(longest, j)