
# Coding question
# Build a function to flatten a compressed string

# Input and output samples:
# ab => ab
# 2[ab] => abab
# 2[a]3[b] => aabbb
# 2[a2[b]] => abbabb
# 2[2[a]2[b]] => aabbaabb
# 2[2[a2[b]]2[c]] => abbabbccabbabbcc

# 2 <= Multiplier < 1000

# O(n) n = length of inputstr
# O(n)

# 10GB file with multiple string, handle?
- assume multiple server
    1. hash the file and spread the file evenly cross server (consistent handling to make load evenly)
    2. solve problem by split the file into multiple strings
    3. merge

- assume multiple server, use message queue
    1. split file into strings, save to database (id, string, status)
    2. spread the work through message queue on multiple server
    3. after processsing, mark COMPLETE on data, and also aggregate the answer


def sol(inputstr):
    stack = []
    cur_str = ''
    cur_num = 0
    res = ''
    for c in inputstr:
        if c.isdigit():
            cur_num = int(c)

        elif c == '[':
            stack.append(cur_str)
            stack.append(cur_num)
            cur_str = ''
            cur_num = 0

        elif c == ']':
            num = stack.pop()
            string = stack.pop()
            cur_str = string + num * cur_str

        else:
            cur_str += c

    return cur_str

# 2[ab] => abab
# 2[a]3[b] => aabbb
# 2[a2[b]] => abbabb
# 2[2[a]2[b]] => aabbaabb
# 2[2[a2[b]]2[c]] => abbabbccabbabbcc

print("2[ab]", sol("2[ab]"))
print("2[a]3[b]", sol("2[a]3[b]"))
print("2[a2[b]]", sol("2[a2[b]]"))
print("2[2[a]2[b]]", sol("2[2[a]2[b]]"))
print("2[2[a2[b]]2[c]]", sol("2[2[a2[b]]2[c]]"))
