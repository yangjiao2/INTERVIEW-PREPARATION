# 2022 SWE interview preparation

Resources:
1. [coding-interview-university](https://github.com/jwasham/coding-interview-university).
2. Algorithms
 - [Algorithms in Python](https://github.com/TheAlgorithms/Python) 
 - [Algorithms in Java](https://github.com/TheAlgorithms/Java).



## Problems & Solutions

[Python](https://github.com/qiyuangong/leetcode/tree/master/python) and [Java](https://github.com/qiyuangong/leetcode/tree/master/java) full list. &hearts; means you need a subscription.

| Category | # | Title | Solution | Basic idea (One line) |
| -- |---| ----- | -------- | --------------------- |
| | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/001_Two_Sum.py) [Java](https://github.com/qiyuangong/leetcode/blob/master/java/001_Two_Sum.java) | 1. Hash O(n) and O(n) space.<br>2. Sort and search with two points O(n) and O(1) space. |
| | 54 | [Spiral matrix](https://leetcode.com/problems/spiral-matrix/) |  | 1. similar to 59 <br> 2. matrix -> array assignment <br> 3. easier for loop traversal with boundary updating from outer to inner matrix  
| | 59 | [Spiral matrix II](https://leetcode.com/problems/spiral-matrix-ii/) | | 1. Set direction with coordinates <br> 2. Loop n*n with boundary check and matrix availability verification
| | 2326 | [Spiral matrix II](https://leetcode.com/problems/spiral-matrix-iv/) | [sol](https://github.com/Yjiao917/2022-SWE-INTERVIEW-PREPARATION/blob/main/Matrix/2326_spiral_matrix_iv.py) | 1. Set direction with coordinates, check boundary and result slot is unset <br> 2. while loop check for head.next != None and assign the lastest value after last run



