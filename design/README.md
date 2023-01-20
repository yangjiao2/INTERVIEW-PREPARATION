
| # | title | idea |
| -- | -- |
| 208 | implement-trie-prefix-tree | 1. add self defined node 2. after loop through, dont need to check index since last node is leaf node already
| [341](https://leetcode.com/problems/flatten-nested-list-iterator/description/) | flatte9n-nested-list-iterator | 1. add custom index using created structure [item, index] 2. when initiation / expand, add [item, 0] and append to list end
| [173](https://leetcode.com/problems/binary-search-tree-iterator/description/) | binary-search-tree-iterator | similar to inorder, add next_node to record current node



hit counter:

- use timestamp % interval to get hits + 1 within limited size array
```
   if (times[idx] != timestamp) {
            times[idx] = timestamp;
            hits[idx] = 1
        } else {
            hits[idx] += 1
        }
```
- if counter[timestamp % interval] != timestamp, that means timestamp has made a new interval loop
```
   if (timestamp - times[i] < 300) {
        res += hits[i];
    }
```
