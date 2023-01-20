def maximumSwap(self, num):
    A = map(int, str(num))
    last = {x: i for i, x in enumerate(A)}
    for i, x in enumerate(A):
        for d in xrange(9, x, -1):
            if last.get(d, None) > i:
                A[i], A[last[d]] = A[last[d]], A[i]
                return int("".join(map(str, A)))
    return num



class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = [int(x) for x in str(num)]
        max_idx = len(num) - 1
        xi = yi = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                xi = i
                yi = max_idx
        num[xi], num[yi] = num[yi], num[xi]
        return int(''.join([str(x) for x in num]))
