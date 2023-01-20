
第一题是括号匹配，第二题是best time to sell and buy stock, leetcode原题。第三题是求解数组立方对的数目。


第一题，给一个数组，判断数组偶数位上的数是否是严格单调增或者减。
第二题突然忘记，如果回想起来会补充。
第三题，给一个数组，判断是否能由[1,2,3,...,n] cyclic shift得到。
第四题，给一个数组a，回复(i,j)的个数，要求a[i]由a[j]最多交换两个数字位置得到。


第一轮给一个streaming系统 问production会有什么问题 这怎么加metrics 怎么mitigate之类的 有过production operation经验的很容易
第二轮设计tunable consistency的datastore
第三轮coding，json parser，类似于https://leetcode.com/discuss/int ... -json-format-string， 挺简单的


1. +/- 运算
2. 数组计算，减掉比之前小的数字，返回所有满足数的和
3. 模拟一个queue队列
4. 根据给定数组建房子，求每一次建完‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌以后最长的连续格子数量，写了union-find超时了， 不知道为啥


python Queue
https://github.com/python/cpython/blob/3.11/Lib/queue.py


```py
def download(queue):
    id = queue.get()
    result = requests.get(f"https://jsonplaceholder.typicode.com/photos/{id}")
    url = result.json()["thumbnailUrl"]
    save_image(id, url)
    print(f"Save image {id}")

NUM_THREADS = 10
q = queue.Queue()
workers = []

for i in range(NUM_THREADS):
    worker = threading.Thread(target=download,args=(q,))
    worker.start()
    workers.append(worker)

for i in range(NUM_THREADS):
    id = random.randint(1,100)
    q.put(id)

for w in workers:
    w.join()

# result:
# Save image 50
# Save image 11
# Save image 16
# Save image 3
# Save image 68
# Save image 81
# Save image 80
```


题目一：给两个数组a跟b以及一个queries，queries包括n个两种操作：[0, i, x]：把b加上x；‍‍‌‍‌‌‌‌‍‌‌‌‌‌‌‍‌‍‌‌[1, x]：找有几个a+b[j]=x的pair。题目需要每当操作[1, x]，把其结果存入一个数组res。最终返回res。
题目二：根据给定数组建房子，求每一次建完以后最长的连续格子数量
题目三：判断一个矩阵是否能放入另一列矩阵
题目四：给一个数组，判断是否能由[1,2,3,...,n] cyclic shift得到
题目五：给一个数组a，回复(i,j‍‍‌‍‌‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌‌‌‌‍‌‌‌‌‌‌‍‌‍‌‌)的个数，要求a由a[j]最多交换两个数字位置得到
题目六：求解数组立方对的数目



第一题：很简单，几分钟就做出来了，所以不太记得了。easy题第二题：类似力口：流逝巴第三题：一个数组里面放入类似与俄罗斯方块的小数组，要求不能重叠。从（0，0）开始放。
第四题：‘+1’ 表示添加1进入数组，‘-1’表示在数组中删除这个数。然后求数组中全部数字平均数。（记‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌不太清楚了）有点类似力口：而舅舞，但题不难，属于中等难度。


第三题：输入一个matrix，“.”代表空，“#”代表盒子，“*”代表障碍物。将matrix翻转90度，盒子在重力作用下掉落在障碍物上，如果没有障碍物则掉落在地面，输出翻转后的matrix，例如输入：
[["#" , "." , "." , "#" , "*" , "." , "."],
["#" , "." , "." , "#" , "." , "." , "."],
["#" , "." , "." , "." , "." , "." , "."]]
结果为：[["." , "." , "#" , "#" , "*" , "." , "."],
["." , "." , "." , "." , "." , "#" , "#"],
["." , "." , "." , "." , "." , "." , "#"]]
输出需要转置。
第四题：输入一个数字列表表示histogram，找到其中面积最大的正方形。如[1,2,3,2,1],面积最大的正方形为2*2; [3‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌,4,3]面积最大的正方形为3*3。



电面
1. recruiter面 过往经历 文化问题 下一份工作的期待 感觉是有一个question list过一遍 不过问的比较详细 比如会问到并发请求数量以及db的承载量问题
2. concurrency面 BufferBoundedQueue 以前面经也有 基本上condition加上mutex实现吧
3. hm面 文化问题加上过往经历 着重在组与组之间的协调和调度
昂赛1
4. operation面 过往设置alert设置metric的经验 处理outage的经验 现场出一个outage的场景 然后看你需要哪些metrics来debug 最后怎样mitigate怎样提action item
5. distributed system面 如何设计分布式键值数据库 如何取舍cap 我基本按照Cassandra那一套设计的
6. coding面 wildcard match
昂赛2
7. recruiter面 文化 性格 处理冲突
8. hm面 过往做project经历 如何处理组内外的关系 如何推动project
9. director面 跨组合作 和pm合作 大规模migration的经验
10. engineer面 如何与同级别enginner合作 对现在工作里的architecture的建议
总的来说 文化和技术基本上同等重要 nflx的文化比较独特 所‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌以是否能够合作推动项目是一个非常重要的考察点


https://www.1point3acres.com/bbs/thread-946694-1-1.html

https://www.1point3acres.com/bbs/thread-953945-1-1.html

Coding - We want to find a shortest path in a warehouse between two products in the warehouse.
1. Give a data model for the warehouse (use a graph. The interviewer asks why not use int[][]? It's because it's very hard to add hallways or small rooms in the int[][] without creating lots of empty space.)
2. Write an algorithm that gives you a shortest path from a to b as an array.
Easy enough.
System Design 1:
Design a commerce model for purchasing (1) access to downloading videos and (2) subscriptions to a video creator.
System Design 2:
Design a contact tracing system like we saw with COVID 19.
1. Have the mobile devices maintain a 2 week rolling log of encounters with others.
2. When someone says they got COVID, retrieve their logs and BFS from those logs with the logs of people they were in contact with. Use Cassandra to keep the logs of people who were in contact.
HM:
Talk about a project you led where you knew it wasn't going to succeed.
Ta‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌lk about a conflict you had with a coworker.
Talk about a conflict you had with your manager.
Talk about your favorite project.
What do you want in your next role.
