

'X' 代表被封锁的道路，你不能穿过。
'D' 代表一个Mart。
給定
city: char[][]

Fullscreen
locations: int[][2]

```py
def solution(city, locations=[(1,2)]):



Design a system that allows DD users to add reviews on ordered food, users will earn rewards based on the quality of the review. For exampel, if number of upvote is 100, user could get 1$, if downvote is 100, user's balance would be decreased 1$.
You need to design t‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌able structure in db, and functions of Restful APIs if possible.


，非常考验inject certain failure后系统还能handle traffic。一定要记住clarify requirements：有多少charity，捐款系统需要运行多少天， QPS多少？



```

在九章里讲过，如果我没记错，是因为第一有些内容需要审核，比如法律相关或者不友好/危险的评论，所以放进message queue里处理了再放出来。另一个也是因为评论后马上看到也不是一个时效性要求很高的需求，所以不需要sync，用asyn也能减少压力。


一开始问了很多问题比如是纯文字的，每人只能对一条review做一种评论，要满足的功能有，评论，查看论评区，修改评论，投票，（可能还有修改投票，但是当时我忘记问了），获得奖励


design food and reward app，就是可以view past orders并可以给他们comment，rate打分。用户可以点赞，超过多少个赞会奖励钱。


review system，要求可以给买的商品写review，每条review可以被upvote和downvote。并且最后可以根据review来给奖励


Design: 三天捐款系統 payment馬上要process 討論非常多如果哪個環節壞掉了要怎麼辦 如何retry etc


非常考验inject certain failure后系统还能handle traffic。一定要记住clarify requirements：有多少charity，捐款系统需要运行多少天， QPS多少？

System design: 购物支付系统后端，客户提交支付信息，后端异步完成交易，提的要求是高容错以及 de-dup，容错基本就是各环节加 r‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌edanduncy 和 retry，de-dup 主要是前端加一个 confirmation 步骤，生成订单 token，正式提交带着 token，后端处理的时候 de-dup 就好了。


```py

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def timestampInBetween(start, end):
    res = []
    d_int = {"mon":1, "tue":2, "wed": 3, "sat":6, "sun":7}

    start_weekday, start_time, start_unit = start.split(" ")
    end_weekday, end_time, end_unit = end.split(" ")

    s_d, e_d = d_int[start_weekday], d_int[end_weekday] if d_int[end_weekday] >= d_int[start_weekday] else d_int[end_weekday] + 8

    s_hr, s_mm = [int(time) for time in start_time.split(":")]
    e_hr, e_mm = [int(time) for time in end_time.split(":")]
    s_hr = int(s_hr) if start_unit == "am" else 12+int(s_hr)
    e_hr = int(e_hr) if end_unit == "am" else 12+int(e_hr)


    print (s_d, e_d, s_hr, e_hr, s_mm, e_mm)
    for d in range(s_d, e_d+1, 1):
        if d = 0:
            continue
        for hh in range(0, 24):
            for mm in range(0, 55, 5):
                if (d == s_d and hh < s_hr) or (d == s_d and hh == s_hr and mm < int(s_mm)):
                    continue
                if (d == e_d and hh > e_hr) or ( d == e_d and hh == e_hr and mm > int(e_mm)):
                    continue
                res.append((d%8)*10000 + hh*100 + mm)

    return res
    
print("sun 10:00 am", "mon 1:00 am", timestampInBetween("sun 10:00 am", "mon 1:00 am"))

```


老题：给（公司名字，坐标），让找出x或y坐标相同的距离最近的公司名字。
解法就是创建从x，y坐标到公司名字的哈西表。



第一道题目是给一个string 和数字k，要求return int 有多少种能将string分成k substrings，并且每一个substring都是palindrome的方法。我用的backtracking，但感觉是不是可以用dp之类的优化。

```py
str1 = 'abbac' ##  ans = 2
str2 = 'cooccooc' ## ans = cooc, c00c




```



find nearest x coordinate or y coordinate city。给一个list of cities 和它们的坐标，再给一个list需要找的city，return 每个city同x或y坐标最近的city。不能用bfs找，直接说了要O(logn)的时间‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌，需要用binary search。最后写完只过了一半的test cases，没时间debug了。

```py
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        res = {'x': [], 'y': []}
        
        for (x2, y2) in points:
            if (x2 == x ) and (not x2 == x and y2 == y):
                res['x'] += 1
            elif ( y2 == y) and (not x2 == x and y2 == y):
                res['y'] += 1
        return  len(e.values())



```




```py

from collections import Counter

def is_permutation(a, b):
    return len(a) == len(b) and Counter(a) == Counter(b)

# Sort both strings
    a = sorted(str1)
    str1 = " ".join(a)
    b = sorted(str2)
    str2 = " ".join(b)
 
    # Compare sorted strings
    for i in range(0, n1, 1):
        if (str1[i] != str2[i]):
            return False




```


design file system



design food and reward app，就是可以view past orders并可以给他们comment，rate打分。用户可以点赞，超过多少个赞会奖励钱。


1235. Maximum Profit in Job Scheduling

```py

    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

      dp = [0] * (len(startTime) + 1)
      jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])


      for i in reversed(range(len(startTime))):
        j = bisect_left(startTime, jobs[i][1])
        dp[i] = max(jobs[i][2] + dp[j], dp[i + 1])

      return dp[0]

```


```py

class Solution:     
    def max_cal(self, prices, calories, budget) -> float:         
        dp = [0] * (budget + 1)         
        for i in range(len(prices)):             
            for j in range(budget, -1, -1):                 
                if j >= prices[i]:                     
                    dp[j] = max(dp[j], dp[j - prices[i]] + calories[i])             
        return dp[-1]



```