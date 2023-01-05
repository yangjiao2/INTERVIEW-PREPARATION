# Example:
# s = 'bcabc'
# last_occ = { a : 2, b : 3, c : 4 }
# stack trace:
# []
# [ 'b' ]
# [ 'b', 'c' ]
# [ 'a' ] (b & c got popped because a < c, a < b and b and c both were gonna repeat in future)
# [ 'a' , 'b' ]
# [ 'a' , 'b', 'c' ]


# Idea:
# last occurance dict
# remove from end of stack if condition met

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

		last_occ = {}
		stack = []
		visited = set()

		for i in range(len(s)):
			last_occ[s[i]] = i

		for i in range(len(s)):

			if s[i] not in visited:
				while (stack and stack[-1] > s[i] and last_occ[stack[-1]] > i):
					visited.remove(stack.pop())

				stack.append(s[i])
				visited.add(s[i])

		return ''.join(stack)
