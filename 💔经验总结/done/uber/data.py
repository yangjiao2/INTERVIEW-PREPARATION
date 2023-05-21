

# AddData(int) RemoveData(int) GetMean() GetMedian() GetModes() (most frequently occuring)
# 3, 8, 9, 3, 8


# AddData(3)

from collections import defaultdict
import heapq

class API:

    def __init__(self):
        self.acc = 0
        self.dic = defaultdict(int)
        self.ctr = 0

        self.max_heap = []
        self.min_heap = []


        # self.freq =
        self.max_freq = 0
        self.most_freq = None
        self.freq_dic = {}

    def addData(self, num):
        self.acc += num
        self.dic[num] += 1
        self.ctr += 1


        if self.dic[num] not in self.freq_dic:
            self.freq_dic[self.dic[num]] = []
        self.freq_dic[self.dic[num]].append(num) # {freq: [nums]}
        if self.dic[num] >= self.max_freq:
            self.most_freq = num
            self.max_freq = self.dic[num]


        top =  self.max_heap[0]
        if (top > num){
            heapq.heappush(self.max_heap, num)
        } else{
            heapq.heappush(self.min_heap, -num)
        }


        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, - heapq.heappop(self.max_heap))


    def removeData(self, num):
        if num not in self.dic or self.dic[num] == 0:
            raise None

        freq = self.dic[num]
        self.acc -= num
        self.dic[num] -= 1
        self.ctr -= 1


        self.freq_dic[freq].remove(num)
        if len(self.freq_dic[freq]) == 0:
            self.freq_dic.pop(freq)
        if self.most_freq == num:
            self.max_freq = max(self.freq_dic.keys())
            self.most_freq = self.freq_dic[ self.max_freq ][0]

        heapq.heappop(self.max_heap, num)
        heapq.heappop(self.min_heap, -num)

    def getMean(self):
        return self.acc / self.ctr if self.ctr != 0 else 0

    def getModes(self):
        return self.most_freq

    def getMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        elif len(self.max_heap)  == len(self.min_heap):
            return (self.max_heap[0] - self.min_heap[0]) / 2
        else:
            return -self.min_heap[0]
