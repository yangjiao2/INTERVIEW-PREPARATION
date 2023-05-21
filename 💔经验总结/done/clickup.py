
# limit < lists

def solution(a, b, limit):
    # limit is larger 2 lens, return sorted lists
    # if limit >= len(set( a + b)):
    #     return (a + b).sort()

    res = []
    # loop 2 lists, check on the first one != res[-1], add; else ignore

    while (limit >= 0 and (len(a) != 0 or len(b) != 0)):
        res_is_empty = len(res) == 0
        if len(a) == 0:
            if res_is_empty or res and b[0] != res[-1]:
                res += b[0],
            b = b[1:]
        elif len(b) == 0:
            if res_is_empty or res and a[0] != res[-1]:
                res += a[0],
            a = a[1:]
        else:
            if a[0] < b[0]:
                if res_is_empty or res and a[0] != res[-1]:
                    res += a[0],
                a = a[1:]
            else:
                if res_is_empty or res and b[0] != res[-1]:
                    res += b[0],
                b = b[1:]

        limit -= 1

    return res


def solution2(a, b, limit):
    # limit is larger 2 lens, return sorted lists
    # if limit >= len(set( a + b)):
    #     return (a + b).sort()

    res = []
    # loop 2 lists, check on the first one != res[-1], add; else ignore

    a_ptr, b_ptr = 0, 0
    while (limit >= 0 and (a_ptr < len(a) or b_ptr < len(b))):
        res_is_empty = len(res) == 0
        if a_ptr >= len(a):
            if res_is_empty or res and b[b_ptr] != res[-1]:
                res += b[b_ptr],
            b_ptr += 1
        elif b_ptr >= len(b):
            if res_is_empty or res and a[a_ptr] != res[-1]:
                res += a[a_ptr],
            a_ptr += 1
        else:
            if a[a_ptr] < b[b_ptr]:
                if res_is_empty or res and a[a_ptr] != res[-1]:
                    res += a[a_ptr],
                a_ptr += 1
            else:
                if res_is_empty or res and b[b_ptr] != res[-1]:
                    res += b[b_ptr],
                b_ptr += 1

        limit -= 1

    return res

a = [-1, 1, 3, 5]
b = [1, 2, 6]
limit = 3

print (solution2(a, b, limit))



a = [-1, 1, 3, 5]
b = [1, 2, 6]
limit = 8

print (solution2(a, b, limit))


a = []
b = [1, 2, 6]
limit = 8

print (solution2(a, b, limit))


a = [2, 2]
b = [1, 2, 6]
limit = 8

print (solution2(a, b, limit))
