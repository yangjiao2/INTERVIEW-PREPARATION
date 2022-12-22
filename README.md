# 2022 SWE interview preparation

Resources:
1. [coding-interview-university](https://github.com/jwasham/coding-interview-university).
2. Algorithms
 - [Algorithms in Python](https://github.com/TheAlgorithms/Python)
 - [Algorithms in Java](https://github.com/TheAlgorithms/Java).
3. [puncsky
/
system-design-and-architecture
](https://github.com/puncsky/system-design-and-architecture)
4. [karanpratapsingh
/
system-design]()
5. Solution: https://github.com/cheonhyangzhang/leetcode-solutions



## 模版

---

Monotonic Queue
```


```



## Problems & Solutions

| Category | Title  | Solution | Basic idea (One line) |
| -- |  ----- | -------- | --------------------- |
| Matrix traversal | [1 Two Sum](https://leetcode.com/problems/two-sum/) | [Py](https://github.com/qiyuangong/leetcode/blob/master/python/001_Two_Sum.py)  | 1. Hash O(n) and O(n) space.<br>2. Sort and search with two points O(n) and O(1) space. |
| Matrix traversal| [54 Spiral matrix](https://leetcode.com/problems/spiral-matrix/) | [Py](https://github.com/Yjiao917/2022-SWE-INTERVIEW-PREPARATION/blob/main/Matrix/54_spiral_matrix.py) | 1. Similar to 59 <br> 2. matrix -> array assignment <br> 3. easier for loop traversal with boundary updating from outer to inner matrix
| Matrix traversal| [59 Spiral matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | [Py](https://github.com/Yjiao917/2022-SWE-INTERVIEW-PREPARATION/blob/main/Matrix/59_spiral_matrix_ii.py) | 1. Set direction with coordinates <br> 2. Loop n*n with boundary check and matrix availability verification
|Matrix traversal | [2326 Spiral matrix II](https://leetcode.com/problems/spiral-matrix-iv/) | [Py](https://github.com/Yjiao917/2022-SWE-INTERVIEW-PREPARATION/blob/main/Matrix/2326_spiral_matrix_iv.py) | 1. Set direction with coordinates, check boundary and result slot is unset <br> 2. while loop check for head.next != None and assign the lastest value after last run
| Interval | [1419 Minimum Number of Frogs Croaking](https://leetcode.com/problems/minimum-number-of-frogs-croaking/) | [Py](https://github.com/Yjiao917/2022-SWE-INTERVIEW-PREPARATION/blob/main/Interval/1419_minimum_number_of_frogs_croaking.py) | 1. Since only whole sentence represents a frog, +1 when first char shows, return -1 when previous char is not appeared <br> 2. Handle corner case: needs to remove uncompleted sentence
| Interval | [1419 Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | [Py](https://github.com/Yjiao917/2022-SWE-INTERVIEW-PREPARATION/blob/main/Interval/2406_divide_into_minimum_number_of_groups.py) | 1. Method 1: minheap to push every element that needs to be counted in a loop <br> 2. Method 2: using line sweep to have cur watermarking the rightmost element within the for loop of the sorted collection
| Dp | [1986 min working hours](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) | [Py]() |
| Hashset | [129 Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/) | [Py](/hashset/128_longest_consecutive_sequence.py) | use hashset to check if in set, then if not visited (x - 1 not in set), loop over to x + i to find longest and update size |
| Mono Queue | [1425 Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/description/) | [Py](/mono%20queue/1425_constrained_subsequence_sum.py) | Use decreasing queue to record summation within `k` constraint 1. calculate summation over current `i` index by adding towards first of decreasing queue 2. if current ele's index is less than `k` constraint, pop left 3. while current ele's summation is more than any previous summation, pop out (right) |
| Counting | [1010 Pairs of Songs ](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/) | [Py](/counting/1010_pairs_of_songs.py) |
2 sum idea: hashset with counteraparts for a given target |
