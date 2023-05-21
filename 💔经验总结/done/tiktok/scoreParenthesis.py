"""
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

s = "()"
out = 1

s = "()()"
out = 2

s = "()(())"
out = 3

s = "(()())"
out = 4

(()) => 2 * () = 2*1 = 2

"""

# (())
# [0, 0]
# [0]
# cur = 1
# cur *= 2

def sol(s):
    stack = []
    cur = 0
    for el in s:
        if el == "(":
            stack.append(cur)
            cur = 0
        else:
            prev = stack.pop()
            cur = prev + max(1, cur * 2)
    return cur
            
print (sol("(()())"), "(()())")
print (sol("()(())"), "()(())")
print (sol("(()(()))"), "(()(()))") # 2 * (1 + 2*1) = 6
print (sol("(()(()))()"), "(()(()))()")

# Time: O(n)
# Space: O(n)




