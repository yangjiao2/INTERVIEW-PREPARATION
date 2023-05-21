https://www.1point3acres.com/bbs/thread-941417-1-1.html


https://www.1point3acres.com/bbs/thread-870800-1-1.html


电面：利口 腰腰寺遛
Onsite：
第一轮：利口 漆凌遛
第二轮：利口 腰寺遛
第三轮：利口 尔尔漆 和 漆漆尔
第四轮：有三个问题，第一题类似 利口 尔石伞，不过不是k个list而是k个文件，文件里每一行是一个数字。第二题利口舞时遛。第三题见下。
第五轮：利口 时 的变种，除了 . *之外还要支持 +
以下是第四轮第三题：
# Same exact input as segment joiner except for now you want to find the segments with an odd number of active segments. A helpful way to think about this is to think of the start index as when someone is born and the end index as when someone dies. You want to output the intervals where an odd number of people are alive
# Sample Input:`[(1,7), (3,5), (4,9)]` should yield ‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌`[(1,3), (4,5), (7,9)]`


https://www.1point3acres.com/bbs/thread-941417-1-1.html



class SnapshotArray(object):
    def __init__(self, n):
        self.cache = [[[-1, 0]] for _ in range(n)]
        self.i = 0

    def set(self, index, val):
        self.cache[index].append([self.i, val])

    def snap(self):
        self.i += 1
        return self.i - 1

    @lru_cache(maxsize=None)
    def get(self, index, snap_id):
        i = bisect.bisect(self.cache[index], [snap_id + 1]) - 1
        return self.cache[index][i][1]


class MyHashMap:
    def __init__(self):
        self.data = [None] * 1000001
    def put(self, key: int, val: int) -> None:
        self.data[key] = val
    def get(self, key: int) -> int:
        val = self.data[key]
        return val if val != None else -1
    def remove(self, key: int) -> None:
        self.data[key] = None




def motion_periods_for_camera(camera_output, threshold):
    res = []
    window_open = False
    for t,v in camera_output:
        if v>=threshold:
            if window_open and res:
                res[-1] = res[-1][0], t
            else:
                res.append((t,t))
            window_open = True
        else:
            window_open = False
    return res

def motion_periods_for_many_cameras(all_cameras, threshold):
    # TODO - Implement me


#     # Example 1
# - Camera 1: [(7, 11)]
# - Camera 2: [(5, 9)]
# - Camera 3: [(7, 17)]
# - Output should be:  [(7, 9)]

# # Example 2
# - Camera 1: [(2, 7), (11, 14)]
# - Camera 2: [(5, 11)]
# - Camera 3: [(1, 21)]
# - Output should be:  [(5, 7), (11, 11)]


    # intervals = [
    #     [(7, 11)], [(5, 9)], [(7, 17)]

    # ]

    intervals = [
        [(2, 7), (11, 14)], [(5, 11)], [(1, 21)]
    ]

    # for camera_output in all_cameras:
    #     intervals.append(motion_periods_for_camera(camera_output, threshold))



    def merge(l1, l2):
        res = []

        while len(l1) > 0  and  len(l2) > 0:
            print (l1, l2)
            end_p =  min(l1[0][1], l2[0][1])
            if l1[0][1] < l2[0][0]:
                l1 = l1[1:]
            elif l2[0][1] < l1[0][0]:
                l2 = l2[1:]
            else:
                print("else", end_p)
                if l1[0][0] < l2[0][0]:
                    res.append((l2[0][0], end_p))
                else:
                    res.append((l1[0][0], end_p))

                if end_p == l1[0][1]:
                    l1 = l1[1:]
                else:
                    l2 = l2[1:]
                print ('?', l1, l2,  len(l1) > 0  and  len(l2) > 0)
        return res

    res = merge(intervals[0], intervals[1])
    print ('--', res)

    if len(intervals) <= 1:
        return res
    for i in range(2, len(intervals)):
        print (i)
        res = merge(res, intervals[i])
    return res

# N = length of timestamp
# Time: O(N)

answer = motion_periods_for_many_cameras(
    [
        [(2, 0.5), (7, 0.8), (10, 0.9), (11, 0.9), (16, 0.4)],
        [(5, 0.8), (8, 0.9), (9, 0.8), (13, 0.5), (20, 0.5)],
        [(6, 0.1), (7, 0.8), (8, 0.9), (17, 0.8)]
    ],
    0.8
)

print("answer", answer)

# assert answer == [(7, 9)]

# answer2 = motion_periods_for_many_cameras(
#     [
#         [(2, 0.9), (7, 0.9), (10, 0.5), (11, 0.9), (14, 0.9)],
#         [(5, 0.9), (11, 0.9)],
#         [(1, 0.8), (8, 0.9), (11, 0.9), (21, 0.9)]
#     ],
#     0.8
# )

# # print(answer2)

# assert answer2 == [(5, 7), (11, 11)]


"""
# Example 1
- Camera 1: [(7, 11)]
- Camera 2: [(5, 9)]
- Camera 3: [(7, 17)]
- Output should be:  [(7, 9)]

# Example 2
- Camera 1: [(2, 7), (11, 14)]
- Camera 2: [(5, 11)]
- Camera 3: [(1, 21)]
- Output should be:  [(5, 7), (11, 11)]
"""
