https://www.youtube.com/playlist?list=PLbhaS_83B97tFPucgkG5gL0OtMzD37lVE


而无益 三思瑶
时间复杂度


伊耳三吴

酒店预定


外星人字典


你为什么选择我们公司？
除了专业，还有什么可以激发你强烈兴趣？



warm up: 125
follow up: 336


题目1 是： 376
题目2是： 890



依依路路，多加了一个callback 方法，要求implement一个interface。



https://www.1point3acres.com/bbs/thread-954110-1-1.html


 伊尔伞舞 饵遥而


https://leetcode.com/problems/fraction-to-recurring-decimal/




class DataStore {
    constructor() {
        this.data = new Map();
        this.change = new Map();
        this.dataEvent = new Map();
    }

    add (name, val) {
        if (this.change.has(name)) {
            if (val != this.data.get(name)) {
                // change happens
                this.change.get(name).call(this, this.data.get(name), val, name);
            }
        }
        if (this.dataEvent.has(name)) {
            this.dataEvent.get(name).call(this, this.data.get(name), val, name);
        }

        this.data.set(name, val);
    }

    has(name) {
        if (this.data.has(name)) {
            return true;
        }
        return false;
    }

    on (event, callbackFn) {
        const p = event.indexOf(':');
        if (p != -1) {
            if (event.substring(0, p) == 'change') {
                this.change.set(event.substring(p+1), callbackFn);
            }
        } else {
            this.dataEvent.set(event, callbackFn);
        }
    }
}

//  test
const ds = new DataStore();
console.log(`ds.add('name', 'Joe')`);
ds.add('name', 'Joe');
console.log(`ds.has("name") = ${ds.has("name")}`);

console.log(`ds.add('age', 30)`);
ds.add('age', 30);
console.log(`ds.has("age") = ${ds.has("age")}`);

console.log(`Sub change:name event`);
ds.on('change:name', (oldVal, newVal, key) => {
    console.log(`The ${key} changes from ${oldVal} to ${newVal}`);
})

console.log(`ds.add('name', 'Tom')`);
ds.add('name', 'Tom');


console.log(`Sub name event`);
ds.on('name', (oldVal, newVal, key) => {
    console.log(`Set ${key} to ${newVal}. The old value is ${oldVal}`);
})

console.log(`ds.add('name', 'Nick')`);
ds.add('name', 'Nick');




https://leetcode.com/problems/flatten-nested-list-iterator/
```py

251. Flatten 2D Vector.py

class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i1 = 0 # outer level index
        self.i2 = 0 # inner level index

        self._moveToValid()

    def _moveToValid(self):
        """
        move i1 and i2 to a valid position, so that self.vec2d[self.i1][self.i2] is valid
        """
        while self.i1 < len(self.vec2d) and self.i2 >= len(self.vec2d[self.i1]):
            self.i1 += 1
            self.i2 = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec2d[self.i1][self.i2]
        self.i2 += 1
        self._moveToValid()

        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i1 < len(self.vec2d)
```


alien dictionary:
建立入度字典 (word[i-1], word[i])



```py

class Solution2(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Find ancestors of each node by DFS.
        nodes, ancestors = set(), {}
        for i in xrange(len(words)):
            for c in words[i]:
                nodes.add(c)
        for node in nodes:
            ancestors[node] = []
        for i in xrange(1, len(words)):
            if (len(words[i-1]) > len(words[i]) and
                    words[i-1][:len(words[i])] == words[i]):
                return ""
            self.findEdges(words[i - 1], words[i], ancestors)

        # Output topological order by DFS.
        result = []
        visited = {}
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""

        return "".join(result)

    # Construct the graph.
    def findEdges(self, word1, word2, ancestors):
        min_len = min(len(word1), len(word2))
        for i in xrange(min_len):
            if word1[i] != word2[i]:
                ancestors[word2[i]].append(word1[i])
                break

    # Topological sort, return whether there is a cycle.
    def topSortDFS(self, root, node, ancestors, visited, result):
        if node not in visited:
            visited[node] = root
            for ancestor in ancestors[node]:
                if self.topSortDFS(root, ancestor, ancestors, visited, result):
                    return True
            result.append(node)
        elif visited[node] == root:
            # Visited from the same root in the DFS path.
            # So it is cyclic.
            return True
        return False

```

pour water: 向左/右找最小， 遇到次高点stop, "fill water"

```java

// Time: O(VN)
// Space: O(1)
class Solution {
public:
    vector<int> pourWater(vector<int>& heights, int V, int K) {
        while (V--) {
            int leftMin = K;
            for (int i = K - 1; i >= 0; --i) {
                if (heights[i] < heights[leftMin]) leftMin = i;
                if (heights[i] > heights[leftMin]) break;
            }
            if (leftMin != K) {
                heights[leftMin]++;
                continue;
            }
            int rightMin = K;
            for (int i = K + 1; i < heights.size(); ++i) {
                if (heights[i] < heights[rightMin]) rightMin = i;
                if (heights[i] > heights[rightMin]) break;
            }
            if (rightMin != K) {
                heights[rightMin]++;
                continue;
            }
            heights[K]++;
        }
        return heights;
    }
};

```
