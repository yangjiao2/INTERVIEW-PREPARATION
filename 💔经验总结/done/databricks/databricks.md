```

 
insert(revenue: int) -> int (auto-incrementing customer id starting at 0)
insert(revenue: int, referrer: int) -> int (auto-incrementing customer id starting at 0)
get_lowest_k_by_total_revenue(k: int, min_total_revenue: int) -> Set<int>
Total revenue = initial revenue + initial revenue of directly referred customers
Example:
insert(10) -> 0   
insert(20, 0) -> 1  
inse‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌rt(40, 1) -> 2
get_lowest_k_by_total_revenue(1, 35) -> (2)
get_lowest_k_by_total_revenue(2, 35) -> (1, 2)

```

```py
import heapq

laptop_costs = {
    'Compaq':499,
    'Dell':530,
    'Apple':999,
    'HP':750,
    'ASUS':650
}

# The 2 cheapest laptops
key_values = zip(laptop_costs.values(), laptop_costs.keys())
print(heapq.nsmallest(2, key_values))
>>> [(499, 'Compaq'), (530, 'Dell')]

# The 2 expensive laptops
key_values = zip(laptop_costs.values(), laptop_costs.keys())
print(heapq.nlargest(2, key_values))
>>> [(999, 'Apple'), (750, 'HP')]

```

```py
class Node():
    def __init__(self, id, rev = 0, referrer = []):
        self.id = id
        self.rev = rev
        self.referrer = referrer

    def add(rev):
        self.rev += rev
        return self

class Solution():

    def __init__(self):
        self.dic = dict[]
        self.heapq = []

    def insert(revenue: int, referrer: int = -1):
        if referrer == -1:
            n = Node(len(self.dic))
            self.dic[len(self.dic)] = n.add(revenue)
        else:
            self.dic[referrer] = self.dic[referrer].add(revenue)
            self.dic[len(self.dic)] = Node(len(self.dic))

        update_heap(heap)

    
    
    def get_lowest_k_by_total_revenue(k: int, min_total_revenue: int):
        for k, v in self.dic.items():
            if v >= min_total_revenue: 
                heappush(self.heapq, (v.rev, k))
            
        while len(self.heapq). > k:
                break

        return list(self.heapq)
        

```

referal level 可以大于1


---


sd: kv store

wal， distributed， sharding， snapshot 回答的磕磕绊绊的但interviewer很nice, multi-thread sodu code




-- 
lazy array

执行这个list of functions然后如果等于targetValue就返回index吗





这一轮是一个coding题目，我拿到的是cache implementation。
从简单的direct map cache开始，你需要存储cache的tag值和value。然后读到的时候再检测。同时你需要一个init variable来看cache是否被init，和dirty bit来看cache是否被写，如果被写才需要evict的时候写入RAM。
然后其实init和dirty bit都可以用bit operation encode到tag里面，然后你需要实现一些bit or，bit add，mask之类的东西。
然后再实现一个fully associative cache，唯一的区别就是，现在每个cache line都可以存到任意entry。但实现到这一步的时候你需要注意tag不再可以encode init & dirty bit。因为你需要整个的address来当tag。






- Lazy array
- BFS related
- Web crawler (multithreading)





面试1 - coding
coding是祖传面试题，revenue。题目大意是databricks有一堆customer，每个customer有对应的revenue。需要支持三个API：
int insert(int revenue)  /* Insert a new customer to the system, with the given revenue. Return the new customer ID */
int insert(int revenue, int referrer)  /* Insert a new customer to the system, with the given revenue, and revenue also added to the referrer. Return the new customer ID */
vector<int> get_lowest_k_by_total_revenue(int k, int min_total_revenue)  /* Get the k customers with the lowest revenue but have revenue above the min_total_revenue. Return the vector of customer IDs that satisfy the condition */
实现思路:
1. write-optimized 如果大部分时间都是insert的话，get_lowest_k_by_total_revenue跑的慢不慢根本无所谓。所以你可以直接用一个array，然后get_lowest_k_by_total_revenue的时候遍历全部。
2. read-optimized 如果大部分时间我们都想读，也就是 get_lowest_k_by_total_revenue。那我们最好maintain一个sorted array。然后每次get的时候binary search for the starting point。
follow-up:
在讲诉完上面的思路之后，面试官让实现了第二种，需要当场跑test cases。在test cases过完之后，也是祖传follow-up，如果我们想算indirect-referer的revenue怎么办。比如 2 refer 1，1 refer 0， 然后我们想算0的overall revenue。输入还包括一个depth，当depth=0就是只算自己，=1就是revenue再加上direct referer。
同样是两种思路:

1. write-optimized 给每个customer记录一个children list，然后只有在get revenue的时候再去用 DFS/BFS 算total revenue
2. read-optimized 每个customer都maintain一个total revenue list， total revenue list每个element对应不同的depth。这个需要你每次insert的时候maintain这个结构，但你在get revenue的时候就可以直接读，不用计算。
面试2 - system design
1个directory里面有很多file，我们需要做的就是计算这个directory里面的word count。每隔一段时间会有一次get word count的操作，同时，会有新的file加进来。目标是尽量快的实现这个过程。
初始思路：
用一个map<string, long>来记录word count。在bootstrap的时候先扫描当前全部file，然后每次get word count的时候再扫描新的file。
优化进程：
1. 文件是sorted by timestamp，可以记录latest timestamp，在扫描新file的时候用类似binary search，直接跳到最新file的位置。
2. 每个file是独立的，可以使用multi-threading来加速，但这设计到一个concurrency write的问题。最好有fine grained的数据结构，但如果没有的话可以用一个global lock解决。global lock比较coarse‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌ grained，所以尽量少call，反应到design上就是先做local word count，再把local word count merge到 global word count。
3. system会crash，可以写中间结果到file里面，然后每次读file来bootstrap。另外的方案是写append-only log，然后每隔一段时间再merge log。
4. 经常写中间结果到file会inefficient，可以记录一个new file count，只有当new file count超过一定的threshold之后才触发。
5. 如果在写中间结果的中途system crash的话，可以自定义一个file terminator，然后读中间结果的时候检测有没有这个terminator，如果有，说明中间结果是正确的写完了的，如果没有则说明这个中间结果不完整，不能使用。






面试题库：浏览了很多面经，这应该是总结最全的一个 https://www.1point3acres.com/bbs/thread-903434-1-1.html
面经：
店面：刷题网摇酒吧，followup是刷题网尔要散，为要注意的区别是有负数如何处理
vo1：architecture， visa payment network （毫不意外）
Lesson: 提前了解下背景知识（https://blog.unibulmerchantservi ... yment-system-works/）和payment system最重要的idempotency要求，剩下的就是正常system design套路了：API design, DB schema, scalability
vo2：algorithms， CIDR（毫不意外）
Lesson: 本轮最后有个bug没找出来（后来发现循环里少写了个break），像这种比较容易出错的coding大家一定要留足时间给testing和debug！他们家非常注重跑通test。以及有些抠细节的题不要以为你做过一遍就能一直做对lol
vo3：design，单机kv store （毫不意外, 但本人非 db相关从业所以觉得依然）
Lesson: 我感觉他家要求你对单机kv store的理解程度是能通过Berkeley自己的cs162课的水平（有空的同学可以找来这个课看看油管有资源），只是浅浅聊WAL/snapshot/读写锁写写伪代码是不够的，还得能回答无数很细节的followup问题比如WAL写到一半如何recover，snapshot写到一半recover。
vo4: coding, Lazy Array （毫不意外），followup是如何用Assertion让unit test变得更加user friendly
Lesson: 提前了解下用Mock + Assertion的方式写unit test会有帮助



电面
通勤方式


1. MockHashMap
2. LazyArray
3. 共享歌单


given a graph of connected nodes, we have to build it by starting with the children that doesn't have any dependencies, we can build nodes concurrently, then return all the bottlenecks. Bottleneck's defined as nodes that have to be bu‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌ilt by themselves due to dependencies. For example, given (A, B), (A, C), (B, D), B is the bottleneck.



topology

b: a
c: a
d: b




def iterator_to_stream(iterator):
    """Convert an iterator into a stream (None if the iterator is empty)."""
    try:
        return iterator.next(), iterator
    except StopIteration:
        return None
Then to extract values from the stream, you just apply stream_next to it, and it will hand you back the next value and the updated state of the stream:

def stream_next(stream):
    """Get (next_value, next_stream) from a stream."""
    val, iterator = stream
    return val, iterator_to_stream(iterator)
Since streams expose their next value, they can be ordered by that value. And for my task that was the property that made all the difference:

import heapq

def merge(iterators):
    """Make a lazy sorted iterator that merges lazy sorted iterators."""
    streams = map(iterator_to_stream, map(iter, iterators))
    heapq.heapify(streams)
    while streams:
        stream = heapq.heappop(streams)
        if stream is not None:
            val, stream = stream_next(stream)
            heapq.heappush(streams, stream)
            yield val
An example use:

>>> xs = merge([xrange(3), xrange(2, 9), xrange(5)])
>>> xs
<generator object merge at 0x7fea07c9d320>

>>> list(xs)
[0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8]



raise AssertionError











import bisect
 
li = [1, 3, 4, 4, 4, 6, 7]
 
# using bisect() to find index to insert new element
# returns 5 ( right most possible index )

print (bisect.bisect_left(li, 4))
assert bisect.bisect(li, 4) == 5, 'bisect test with test case: {input}'.format(input= [4])


from heapq import heappush, heappop

def getroute(routes):
    if not routes or not routes[0]:
        print ('finish')
        return 
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    heap = []

    def findcell(routes, value):
        return [(ri, ci) for ri, r in enumerate(routes) for ci, c in enumerate(r) if routes[ri][ci] == value]

    s, e = findcell(routes, 's'), findcell(routes, 'e')

    if not s:
        raise ValueError('routes')
    # for d in directions:
    #     x, y = s[0]+d[0], s[1]+d[1]

    # m, n = len(routes), len(routes[0])

print(getroute([['s']]))










AutoComplete widget

https://www.1point3acres.com/bbs/thread-922466-1-1.html   
https://www.1point3acres.com/bbs/thread-882989-1-1.html   
https://www.1point3acres.com/bbs/thread-796926-1-1.html

2. 怎么debounce

3. 怎么fetch data，handle error
4. 如果request返回顺序打乱怎么处理 （我的答案是fetch结果也返回使用的keyword，这样promise resolve的时候比较使用的keyword和最新的keyword是否一致，一致才render，不一致说明是之前的request，直接discard）
5. 如果request很慢怎么办，答：ghost card，timeout
6. 怎样设计widget使得可以支持除了restful api 之外的数据，答：dataset 接口，通用返回 Promise<string[]>，这样widget consumer可以自己实现 data fetch
另外还有两道其他坛友遇到的，一并总结在这：
1. 設計一個可以多人同步編輯的 music play list   
https://www.1point3acres.com/bbs/thread-818999-1-1.html   
2. 问了几个 javascript closure  的小问题，然后用 css 和 vanilla js 写了一个 comment list，不需要考虑 recursion  ‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌
https://www.1point3acres.com/bbs/thread-768536-1-1.html   