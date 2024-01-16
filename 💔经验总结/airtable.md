system design
是做一个search engine，要特别强调scalable


然后给一个target task，完成两个function。
1. List<String> init(target)  返回如果要完成这个target，有哪些tasks现在可以开始做。（也就是没有任何dependent）


from collections import defaultdict

def solution(inputs, start='a'):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    res = []

    for n1, n2 in inputs: # O(E)
        graph[n1].append(n2)
        # indegree[n2] += 1
        # indegree[n1] += 0

    q = [start]
    # print (graph)
    while q:
        node = q.pop(0)
        # print (node, indegree)
        for nei in graph[node]:
            if nei not in graph:
                res += nei,
            else:
                # indegree[nei] -= 1
                q.append(nei)

2. List<String> onComplete(task) 返回如果完成task，有哪些tasks被unblock。（也就是完成当前task，哪些被u‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌nblock）

def get_dependent_nodes(graph, x):
    dependent_nodes = []
    for edge in graph:
        if edge[1] == x:
            dependent_nodes.append(edge[0])
    return dependent_nodes



地里原题dag遍历和拓扑排序，讲真电面这种题是不是有点不太合理… 给一个adjacency map，需要实现两个function。第一个是给node，把这个node当做树的根节点去找leaf，dfs即可。注意第二问不需要对全部node拓扑排序，只需要对target node找深一层即可，构建完d‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌egree map之后不需要queue。


Coding
给定一个build dependency. 实现下面两个function E.g.
        a
b          c             f
d                   e
   start( 任意 node )  -> return 所有现在能开始build的node
   vector<Node> Complete( vector<Node> input)  -> 假设input list里面所有的node都complete之后，return 下一步有哪些node可以开始build. 假‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌设complete 的input是valid的，每个node只会被complete一次.
比如
start(a) // return d, e
complete(d) // return b, 之前return过的e在这里不需要return


给一个build dependency graph，比如：
{
  {"foo.h", {}},
  {"bar.h", {}},
  {"foo.o", {"foo.h"}},
  {"bar.o", {"bar.h"}},
  {"bin", {"foo.o", "bar.o"}}
}
实现两个函数：
1) Init(string target)：返回当前能够开始build的一些build targets
2) OnComplete(string target): 返回当target已经build完后，哪些新的build targets变得可以开始build
比较容易，明显的DAG遍历。


foo.h           bar.h
foo.0           bar.o
        bin

init:



609. Find Duplicate File in System
如果文件很多怎么办，文件很大怎么办
```py

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        contents = collections.defaultdict(list)
        for l in paths:
            path, files = l.split(' ', 1)
            print (path, ', ', files)
            for f in files.split(" "):
                # fname = f[:f.index("(")]
                # content = f[f.index("(") + 1 : -1]
                fname, _, content = f[:-1].partition("(")
                contents[content].append(path.strip()+"/"+fname)

        res = []
        print (contents)
        for c, paths in contents.items():
            if len(paths) >= 2:
                res += [paths]

        return res

```







Data structure and algorithm design
功能设计：公式
怎么读用户给的字符串，里面有数字加运算符，类似李口而尔丝，包括括号加减乘除
API设计，怎么传backend，有哪几种方法，tradeoff
如何触发计算，如何并发计算5000+列
db怎么存
通信协议 tradeoff http websocket long polling
怎么解决列之间dependency，比如 C= Ａ＋Ｂ，F＝Ｃ* D
如果有condition怎么解决，if/else/while
2. Feature/API Design
功能设计：mention
db schema。怎么存，有几种存法，tradeoff
设计API， tradeoff
API如何向后兼容
如何保证用户在不同系统，设备上的一致体验，比如用户一会儿ios 一会儿mac client
3. Programming
给起始日期，项目需要的天数，list of holidays，求项目截止日期，要求优化比O（N）要好
4. Designing a backend service
上来口述李口散死就的解法，然后扩展到n array，follow up如果array过大怎么办，如果一个array大另一个小怎么办
非常规系统设计，给了search engine的component，client， query engine， inverted index，问inverted index的sharding方法
剩下时间讨论tradeoff，主要就是term based vs document based，可以参考Jeff Dean的slides http://videolectures.net/wsdm09_dean_cblirs/



1. 怎么存储formula
2. 怎么设计event feeds的UI
3. 设计mentions功能



- coding get working days
事后知道execl有这个function，可能研究一下details或许有帮助。面试不需要跑。我个人觉得我的问题是 实现bruteforce时候有点慢，然后后面的复杂度分析的不太好（这个可能是我的弱项）。这轮positive
- system design search engine
有个帖子给了图，就是那个题。给很多信息 不是传统的system design让你加component。开始让我写了两个算法 1. intersection of 2 array 2. intersection of n array
然后开始开放式的问各种问题。n array的big O 蠢了 忘了N和len of array是两个参数。然后后面distributed system 各种tradeoff讨论的不好。面试官是MIT+standford PHD，有点不是那么好交流。这轮NO
- product design @mention
数据库 API的设计。讨论了很多backward compatible， support new/old/different versions of clients。 这轮知识比较comfortable，答得也还行，positive。
- product design formula
有想到AST啊什么的， 但是我并不是很懂，只知道概念。后面问了些security相关的概念，问到我的盲区了。feedback是mixed，不够strong，有知识但是对于com‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌plex的问题和security的考虑不够。






class ModifiableSetIterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self):
        if self.index < len(self.container):
            self.index += 1
            return self.container[self.index - 1]
        raise StopIteration

    def set_value(self, value):
        if 0 <= self.index < len(self.container):
            self.container[self.index] = value

    def erase_value(self):
        if 0 <= self.index < len(self.container):
            del self.container[self.index]
            self.index = max(0, self.index - 1)


class ModifiableSet:
    def __init__(self):
        self.data = []
    
    def __iter__(self):
        return ModifiableSetIterator(self.data)
    
    def add(self, value):
        if value not in self.data:
            self.data.append(value)
    
    def __contains__(self, value):
        return value in self.data
    
    def __len__(self):
        return len(self.data)
    
    def __str__(self):
        return str(self.data)


# Example usage
s = ModifiableSet()
s.add(10)
s.add(20)
s.add(30)

print("Original set:", s)

iterator = iter(s)
next(iterator)  # Points to 10
iterator.set_value(15)
next(iterator)  # Points to 20

print("Set after modifying value:", s)

iterator.erase_value()

print("Set after erasing value:", s)









import bisect
 
li = [1, 3, 4, 4, 4, 6, 7]
 
# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print ("Rightmost index to insert, so list remains sorted is : ",
       end="")
print (bisect.bisect(li, 4))
assert bisect.bisect(li, 4) == 5, 'bisect test with test case: {input}'.format(input= [4])


