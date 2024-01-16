def solution(input1):
    result = []
    answered_set = set()
    unanswered_set = set()

    for i, (answered, dep, unanswered_dep) in enumerate(input1):
        if all(e in result and input1[e][0] for e in dep) and all(e not in result and not input1[e][0] for e in unanswered_dep):
            result.append(i)

            if answered:
                answered_set.add(i)
            else:
                unanswered_set.add(i)

    return result

# Test Case 1
input1 = [
    [False, [3], []],
    [True, [], [0]],
    [True, [], [1]],
    [True, [1, 2], []]
]
expected_output1 = [1]
output1 = solution(input1)
assert output1 == expected_output1, f"Test Case 1 failed: expected {expected_output1}, got {output1}"

# Test Case 2
input2 = [
    [True, [], []],
    [False, [0], []],
    [True, [1], []],
    [False, [0, 2], []]
]
expected_output2 = [0, 1]
output2 = solution(input2)
assert output2 == expected_output2, f"Test Case 2 failed: expected {expected_output2}, got {output2}"

# Test Case 3
input3 = [
    [True, [], [1, 2]],
    [False, [2], []],
    [True, [], []],
    [False, [0, 2], [1]]
]
expected_output3 = [1, 2]
output3 = solution(input3)
assert output3 == expected_output3, f"Test Case 3 failed: expected {expected_output3}, got {output3}"

print("All test cases passed.")
